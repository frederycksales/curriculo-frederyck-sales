#!/usr/bin/env python3
"""
Conversor de Markdown para PDF - Trabalho DevSecOps
Suporta múltiplos métodos de conversão
"""

import os
import sys
import subprocess
from pathlib import Path

def check_command(cmd):
    """Verifica se um comando está disponível no sistema"""
    try:
        subprocess.run([cmd, '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def method_1_pandoc(input_file, output_file):
    """
    Método 1: Pandoc (RECOMENDADO)
    - Melhor qualidade de conversão
    - Suporta tabelas complexas, code blocks, etc
    - Requer: pandoc + texlive-xetex
    """
    print("\n🔷 Método 1: Usando Pandoc")
    
    if not check_command('pandoc'):
        print("❌ Pandoc não encontrado!")
        print("   Instale com: sudo apt install pandoc texlive-xetex")
        return False
    
    try:
        # Comando pandoc com configurações otimizadas
        # geometry aceita especificação de papel e margens, ex: 'a4paper,margin=1.5cm'
        geometry_value = f"{PAPER_SIZE_PANDOC},margin={MARGIN_CM}cm"
        
        cmd = [
            'pandoc',
            input_file,
            '-o', output_file,
            '--pdf-engine=xelatex',
            '--variable', f'geometry:{geometry_value}',
            '--variable', 'fontsize=11pt',
        ]
        
        # Configurações específicas por tipo de documento
        if DOCUMENT_TYPE == 'academic':
            cmd.extend([
                '--variable', 'linestretch=1.5',
                '--toc',  # Table of Contents
                '--toc-depth=2',
                '--highlight-style=tango',  # Syntax highlighting
                '-V', 'colorlinks=true',
                '-V', 'linkcolor=blue',
                '-V', 'urlcolor=blue',
            ])
        else:  # resume/cv
            cmd.extend([
                '--variable', 'linestretch=1.15',  # Espaçamento mais compacto
                '--variable', 'fontsize=10pt',  # Fonte um pouco menor
                '-V', 'colorlinks=true',
                '-V', 'linkcolor=black',  # Links discretos
                '-V', 'urlcolor=blue',
            ])
        
        print(f"   Executando: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ PDF gerado com sucesso: {output_file}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar pandoc: {e.stderr}")
        return False

def method_2_weasyprint(input_file, output_file):
    """
    Método 2: WeasyPrint (Python puro)
    - Não requer LaTeX
    - Converte Markdown → HTML → PDF
    - Requer: pip install markdown weasyprint
    """
    print("\n🔷 Método 2: Usando WeasyPrint (Python)")
    
    try:
        import markdown
        from weasyprint import HTML, CSS
    except ImportError:
        print("❌ Bibliotecas não encontradas!")
        print("   Instale com: pip install markdown weasyprint")
        return False
    
    try:
        # Ler o arquivo Markdown
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Converter Markdown para HTML
        html_content = markdown.markdown(
            md_content,
            extensions=[
                'tables',
                'fenced_code',
                'codehilite',
                'toc',
                'sane_lists'
            ]
        )
        
        # CSS específico por tipo de documento
        if DOCUMENT_TYPE == 'academic':
            body_css = """
                body {
                    font-family: 'Liberation Serif', 'DejaVu Serif', serif;
                    font-size: 11pt;
                    line-height: 1.6;
                    color: #333;
                }
                h1 {
                    font-size: 20pt;
                    color: #1a1a1a;
                    border-bottom: 2px solid #333;
                    padding-bottom: 10px;
                }
                h2 {
                    font-size: 16pt;
                    color: #2a2a2a;
                    margin-top: 20px;
                    border-bottom: 1px solid #999;
                }
                h3 {
                    font-size: 13pt;
                    color: #3a3a3a;
                }
                code {
                    background-color: #f4f4f4;
                    padding: 2px 5px;
                    border-radius: 3px;
                    font-family: 'DejaVu Sans Mono', monospace;
                    font-size: 9pt;
                }
                pre {
                    background-color: #f4f4f4;
                    padding: 10px;
                    border-radius: 5px;
                    overflow-x: auto;
                    font-size: 9pt;
                }
            """
        else:  # resume/cv
            body_css = """
                body {
                    font-family: 'Liberation Sans', 'DejaVu Sans', Arial, sans-serif;
                    font-size: 10pt;
                    line-height: 1.3;
                    color: #2c3e50;
                }
                h1 {
                    font-size: 22pt;
                    color: #1a1a1a;
                    margin-bottom: 5px;
                    margin-top: 0;
                }
                h2 {
                    font-size: 14pt;
                    color: #2c3e50;
                    margin-top: 15px;
                    margin-bottom: 8px;
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 3px;
                }
                h3 {
                    font-size: 11pt;
                    color: #34495e;
                    margin-top: 10px;
                    margin-bottom: 5px;
                    font-weight: bold;
                }
                h4 {
                    font-size: 10pt;
                    color: #555;
                    margin-top: 8px;
                    margin-bottom: 3px;
                }
                p {
                    margin: 3px 0;
                }
                ul {
                    margin: 5px 0;
                    padding-left: 20px;
                }
                li {
                    margin: 2px 0;
                }
                code {
                    background-color: #ecf0f1;
                    padding: 1px 4px;
                    border-radius: 2px;
                    font-family: 'DejaVu Sans Mono', monospace;
                    font-size: 9pt;
                    color: #c7254e;
                }
                strong {
                    color: #2c3e50;
                }
                a {
                    color: #3498db;
                    text-decoration: none;
                }
                hr {
                    border: none;
                    border-top: 1px solid #bdc3c7;
                    margin: 10px 0;
                }
            """
        
        # Adicionar CSS para melhor formatação
        # Ajustar tamanho de página e margens via @page
        styled_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                @page {{
                    size: {PAPER_SIZE};
                    margin: {MARGIN_CM}cm;
                }}
                {body_css}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 15px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                    font-weight: bold;
                }}
                blockquote {{
                    border-left: 4px solid #ddd;
                    padding-left: 15px;
                    color: #666;
                    font-style: italic;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Converter HTML para PDF
        HTML(string=styled_html).write_pdf(output_file)
        print(f"✅ PDF gerado com sucesso: {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def method_3_md2pdf(input_file, output_file):
    """
    Método 3: md2pdf (Python - Simples)
    - Mais simples, mas menos features
    - Requer: pip install md2pdf
    """
    print("\n🔷 Método 3: Usando md2pdf")
    
    try:
        from md2pdf.core import md2pdf
    except ImportError:
        print("❌ Biblioteca md2pdf não encontrada!")
        print("   Instale com: pip install md2pdf")
        return False
    
    try:
        # md2pdf accepts a css file for styling; we will generate a small CSS to set page size/margins
        css_temp = None
        try:
            import tempfile
            css_temp = tempfile.NamedTemporaryFile(delete=False, suffix='.css')
            css_content = f"""
            @page {{ size: {PAPER_SIZE}; margin: {MARGIN_CM}cm; }}
            body {{ font-family: 'DejaVu Serif', serif; font-size:11pt; line-height:1.5; }}
            """
            css_temp.write(css_content.encode('utf-8'))
            css_temp.flush()

            md2pdf(
                output_file,
                md_file_path=input_file,
                css_file_path=css_temp.name,
                base_url=None
            )
        finally:
            if css_temp:
                try:
                    css_temp.close()
                except Exception:
                    pass
        print(f"✅ PDF gerado com sucesso: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def method_4_pypandoc(input_file, output_file):
    """
    Método 4: PyPandoc (Python wrapper para Pandoc)
    - Combina Python + Pandoc
    - Requer: pip install pypandoc + pandoc instalado
    """
    print("\n🔷 Método 4: Usando PyPandoc")
    
    try:
        import pypandoc
    except ImportError:
        print("❌ Biblioteca pypandoc não encontrada!")
        print("   Instale com: pip install pypandoc")
        return False
    
    if not check_command('pandoc'):
        print("❌ Pandoc não encontrado (necessário para pypandoc)!")
        print("   Instale com: sudo apt install pandoc texlive-xetex")
        return False
    
    try:
        geometry_value = f"{PAPER_SIZE_PANDOC},margin={MARGIN_CM}cm"
        pypandoc.convert_file(
            input_file,
            'pdf',
            outputfile=output_file,
            extra_args=[
                '--pdf-engine=xelatex',
                f'--variable=geometry:{geometry_value}',
                '--variable=fontsize=11pt',
                '--toc',
                '--highlight-style=tango'
            ]
        )
        print(f"✅ PDF gerado com sucesso: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def main():
    """Função principal"""
    
    print("=" * 70)
    print("📄 CONVERSOR MARKDOWN → PDF (Modo Simplificado - CV)")
    print("=" * 70)
    
    # Arquivo de entrada via argumento ou prompt
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        print(f"\n📥 Arquivo de entrada: {input_file}")
    else:
        input_file = input("\n📥 Digite o caminho do arquivo Markdown (.md): ").strip()
        if not input_file:
            print("❌ Nenhum arquivo fornecido!")
            sys.exit(1)
    
    # Configurações fixas para CV
    global DOCUMENT_TYPE, PAPER_SIZE, MARGIN_CM, PAPER_SIZE_PANDOC
    DOCUMENT_TYPE = 'resume'
    PAPER_SIZE = 'OFFICIO'
    MARGIN_CM = 1.5
    PAPER_SIZE_PANDOC = 'paperwidth=216mm,paperheight=330mm'
    
    print("✓ Formato: Currículo Profissional")
    print(f"✓ Papel: {PAPER_SIZE} (216x330mm)")
    print(f"✓ Margens: {MARGIN_CM}cm")
    print("✓ Método: Pandoc")
    
    # Verificar se arquivo existe
    if not os.path.exists(input_file):
        print(f"\n❌ Arquivo não encontrado: {input_file}")
        print(f"   Certifique-se de executar o script na pasta: {os.getcwd()}")
        sys.exit(1)
    
    # Arquivo de saída
    output_file = str(Path(input_file).with_suffix('.pdf'))
    
    print(f"\n Arquivo de saída: {output_file}")
    
    # Executar conversão com Pandoc direto
    if not method_1_pandoc(input_file, output_file):
        print("\n❌ Conversão falhou.")
        print("   Certifique-se que o Pandoc está instalado:")
        print("   sudo apt install pandoc texlive-xetex")
        sys.exit(1)
    
    # Verificar se arquivo foi criado
    if os.path.exists(output_file):
        file_size = os.path.getsize(output_file) / 1024  # KB
        print(f"\n✅ Sucesso! PDF gerado: {output_file} ({file_size:.1f} KB)")
        print(f"   Abra com: xdg-open {output_file}")
    else:
        print(f"\n❌ Erro: arquivo {output_file} não foi criado")
        sys.exit(1)

if __name__ == "__main__":
    main()

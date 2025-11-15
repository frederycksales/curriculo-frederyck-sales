**Frederyck Baleeiro Espinheiro Sales**

**Site Reliability Engineer (SRE) | Observability Engineer - English Fluent (B2/C1)**  
**(91) 9 9221-2185 • <frederyck.sales@hotmail.com> • [LinkedIn](https://linkedin.com/in/frederyck-baleeiro-espinheiro-sales-4836b4125) • [GitHub](https://github.com/frederycksales) • Castanhal – Pará**

---

## Apresentação

**Site Reliability Engineer (SRE)** com **2 anos de experiência especializada em Observabilidade e práticas de confiabilidade**, construindo base sólida em sistemas distribuídos e monitoramento de alta performance. Responsável pela implementação e operação de stack completa de monitoramento (Prometheus, Grafana, Loki, Zabbix, Elasticsearch), com foco em **automação (Ansible, Terraform)**, **IaC**, **GitOps** e métricas de confiabilidade (SLIs/SLOs). Background de **7 anos em TI** fornece perspectiva ampla sobre suporte, troubleshooting e impacto na experiência do usuário.

**Conquistas e Aprendizados:**

- Implementação bem-sucedida de **alertas baseados em SLIs/SLOs** que resultaram em **redução de 80%+ no ruído de alertas** em ambiente com **400+ hosts monitorados**, aplicando Processo de Gestão de Eventos.
- Contribuição para **99% de disponibilidade** dos serviços de monitoramento **suportando usuários 24/7**, através da aplicação de práticas de IaC, staging environments e GitOps.
- Desenvolvimento de **automação com Ansible** que acelerou provisionamento de servidores de horas para minutos, aplicando conceitos de infraestrutura como código e eliminando erros de configuração manual.
- Aprendizado prático em **redução de incidentes críticos** através de avaliações de conformidade automatizadas e construção de playbooks/runbooks de remediação.

---

## Educação

**Especialização em Site Reliability Engineering (SRE)** | PUC Minas | 2025 – 2026 (Em Andamento)

**Bacharel em Engenharia Elétrica** | Universidade Estácio de Sá | 2020 – 2024 (Concluído)  
*Ênfase em Sinais e Sistemas, Estatística e Modelagem Computacional. TCC em Machine Learning aplicado a sistemas elétricos.*

---

## Experiência Profissional

### Encarregado de NOC - Observabilidade | Sea Telecom

**Jul 2023 – Atual (2 anos 4 meses) | Castanhal, PA | Presencial**

Responsável pela implementação e operação da stack de monitoramento e práticas de observabilidade, atuando de forma autônoma no desenvolvimento técnico e administração da infraestrutura relacionada. Reportando diretamente à gerência de NOC, tenho aplicado e expandido conhecimentos em SRE através de projetos práticos e implementações reais.

#### IMPLEMENTAÇÃO DE OBSERVABILIDADE E PRÁTICAS SRE

**Stack de Monitoramento e Observabilidade:**

- Implementei e opero stack de observabilidade: **Prometheus (Mimir como TSDB)**, **Grafana**, **Loki**, **Zabbix**, **Elasticsearch** e **Rsyslog**.
- Administro infraestrutura de suporte: bancos de dados **PostgreSQL** e **MySQL** dedicados, **exporters customizados** (Node Exporter, fping-exporter desenvolvido internamente), **Nginx** como proxy reverso.
- **Otimização de performance do Zabbix Server:** Aplicação de tuning em parâmetros de configuração (`zabbix_server.conf`), ajuste de processos internos (pollers, trappers, history syncers) e otimização de queries de banco de dados para suportar 400+ hosts monitorados.
- **Desenvolvimento de exporters Prometheus:** Criação de fping-exporter customizado para coleta de métricas de latência de rede em larga escala.
- Construí dashboards focados em **SLIs/SLOs** baseados em **Golden Signals** (Latência, Tráfego, Erros, Saturação), aprendendo a traduzir métricas técnicas em indicadores de negócio.
- Contribuí para **redução de 80%+ no ruído de alertas**, permitindo que a equipe foque em incidentes de alto impacto.
- Participei da **melhoria de 40%+ no MTTD** (Mean Time to Detect) de incidentes críticos através de implementação de alertas mais precisos.

**Práticas de Confiabilidade & Gestão de Incidentes:**

- Realizo **RCA (Root Cause Analysis)** e participo de **Blameless Post-mortems** para aprendizado contínuo e prevenção de recorrência.
- Aplico conceitos de **SLIs, SLOs e SLAs** para medir e melhorar a confiabilidade dos serviços.
- **Planejamento de capacidade:** Realizei análise de crescimento de TSDB com projeção de uso até 2026 utilizando modelagem estatística, implementando estratégia de remote write para Mimir que resultou em redução de 80% no storage local.
- **Design de Dashboards:** Criação de dashboards orientados a SLIs para infraestrutura L1/L2, otimizando visibilidade de incidentes para NOC operando em modelo home office.
- Implementação de observabilidade para rede multivendor (Huawei, Datacom, Fiberhome, ZTE) via **SNMP**.
- Contribuí para **99% de disponibilidade** e redução de incidentes críticos anuais através da aplicação de práticas de confiabilidade e automação.

#### AUTOMAÇÃO E INFRAESTRUTURA COMO CÓDIGO (IaC)

**Automação com Ansible:**

- Desenvolvi **framework de automação com 10+ roles reutilizáveis** (PostgreSQL, MariaDB, MongoDB, Zabbix, GLPI, MinIO) aplicando templates Jinja2, handlers e gestão de serviços via systemd.
- Criação de **15+ playbooks** para deploy, troubleshooting e remediação automatizada (fix-readonly-filesystem, diagnose-filesystem, deploy-observability-stack).
- Alcancei **redução de provisionamento de servidores de horas para minutos**, eliminando a maioria dos erros de configuração manual através de inventários estruturados e validação de estado.
- Implementação de práticas de **IaC** com **Terraform** e **Ansible** para versionamento e reprodutibilidade de ambiente.

**Desenvolvimento de Ferramentas Python:**

- **NetBox-Zabbix Comparator:** Ferramenta CLI para auditoria de inventário entre NetBox (Source of Truth) e Zabbix, com análise de discrepâncias (IP conflicts, status), testes de conectividade ICMP e exportação de relatórios executivos em Excel. Arquitetura em camadas com 15 componentes desacoplados, build automation (PyInstaller) e code quality (Black, Ruff).
- **CPE Onboarding/Offboarding Automation:** Sistema de automação para gestão do ciclo de vida de CPEs entre NetBox e Zabbix, com normalização de dados (DBML schema), validações de conformidade, backup/rollback de operações e rastreabilidade via logs estruturados.
- **Grafana CLI Tool:** Aplicação para gestão de backups de dashboards com estrutura profissional (pyproject.toml, testes automatizados).
- **SSH Orchestrator:** Ferramenta para orquestração de comandos em múltiplos hosts com logging estruturado e configuração modular.
- **Backup Automation:** Sistema para Wiki.js (PostgreSQL dump + upload MinIO) com retry logic e notificações.
- **Prometheus Exporters:** Desenvolvimento de fping-exporter customizado para métricas de latência de rede.
- **Zabbix Log Analyzer:** Ferramenta de troubleshooting para análise de erros SNMP com dashboards KPI (Rich library), análise estatística e identificação de padrões temporais.
- Automação de hardening de segurança em servidores Linux: aplicação de patches, auditoria de acessos e implementação de controles.

**Infraestrutura:**

- Administração de infraestrutura **on-premise (OpenStack)**: provisionamento, configuração, monitoramento e manutenção de VMs Linux.
- **Containerização de serviços:** Deploy e orquestração de stacks com Docker Compose (LGTM stack, Observability stack com Loki+Mimir+MinIO+Grafana Alloy). Estudando migração para Kubernetes em ambiente de staging (ConfigMaps, Secrets, Ingress controllers).
- **Reverse Proxy:** Configuração de Nginx para múltiplos serviços com SSL/TLS, rate limiting e load balancing.
- Versionamento de configurações e scripts com **Git/Gitea**.
- Administração de **Wiki.js** como plataforma central de documentação técnica (incluindo backups automatizados e disaster recovery).

#### APRENDIZADO E DESENVOLVIMENTO TÉCNICO

- Participação ativa em iniciativas de melhoria contínua e adoção de práticas modernas de SRE no time de NOC.
- **Proposta Técnica SRE:** Elaboração de proposta técnica em LaTeX (padrão ABNT) com diagramas C4 (PlantUML) para arquitetura de solução, planejamento de implantação, indicadores de ROI e estratégia de SLIs/SLOs/Error Budgets.
- Estudos de viabilidade para migração para nuvem pública (**AWS**, GCP) e adoção de SaaS (Grafana Cloud, Netdata), incluindo análise de custos com AWS Pricing Calculator e comparativos de TCO (Total Cost of Ownership).
- Planejamento de implementação de processos baseados em **ITIL** com **GLPI**.
- Aplicação de métricas de desempenho (**MTTD, MTTR**) para orientar melhorias e decisões técnicas.

**Tecnologias:** Prometheus (Mimir) • Grafana • Loki • Zabbix • Elasticsearch • Rsyslog • OpenStack • Docker • Linux (Debian/Ubuntu) • PostgreSQL • MySQL • Nginx • Python • Ansible • Terraform • Bash • Git/Gitea • GLPI • Wiki.js • Jenkins

---

### Encarregado de SAC | Sea Telecom

**Set 2022 – Jul 2023 (11 meses) | Castanhal, PA | Presencial**

Coordenação de equipes de suporte técnico, evoluindo de gestão geral para coordenação de especialistas focados em casos críticos. Experiência que proporcionou compreensão sobre gestão de incidentes e impacto no usuário final, fundamentais para a transição para SRE.

**Principais Realizações:**

- Participação ativa durante **incidentes de serviço**, coordenando resposta e minimizando impacto no cliente.
- Implementação de análise de dados baseada em **KPIs** (**Power BI**) para otimizar processos, contribuindo para **redução de 25% no tempo de resolução**.
- Aplicação de princípios **Lean** e **Kanban** para gerenciar fluxo de demandas.
- Utilização de ferramentas analíticas (**5 Porquês**, **Matriz de Prioridade**, **Análise SWOT**) para identificar e eliminar gargalos.

**Tecnologias:** Power BI • Excel • Lean (Kanban, 5 Porquês) • Gestão de Incidentes • ITIL

---

### Assistente de SAC | Sea Telecom

**Fev 2022 – Dez 2022 (11 meses) | Castanhal, PA | Presencial**

Diagnóstico e resolução de problemas de conectividade em redes FTTH, aprofundando compreensão sobre impacto da estabilidade na experiência do usuário.

**Principais Realizações:**

- Análise de dados de atendimento com **Power BI** e **Python** (Pandas, NumPy, Jupyter Notebook) para identificar tendências e padrões de falhas.
- Fornecimento de insights para melhoria contínua dos serviços.
- Treinamento técnico para novos colaboradores.

**Tecnologias:** Power BI • Python (Pandas, NumPy, Jupyter Notebook) • FTTH • Troubleshooting

---

### Operador de Telemarketing | Sea Telecom

**Set 2020 – Fev 2022 (1 ano 6 meses) | Castanhal, PA | Presencial**

Suporte técnico para serviços de banda larga FTTH, construindo base técnica em redes e diagnóstico.

**Principais Realizações:**

- Diagnóstico de rede: análise de latência, desconexão, DNS, DHCP usando Ping, Traceroute e análise de logs.
- Utilização de ferramentas de NMS: **NETNUMEN (ZTE)** e **UNM (FiberHome)** para configuração, analise de performance e saúde de dispositivos da rede GPON.
- Configuração de equipamentos de rede (roteadores ZTE, FiberHome, TP-Link): SSID, WPA2, QoS, VLANs.

**Tecnologias:** FTTH • NETNUMEN/UNM • DNS/DHCP • QoS/VLANs • Troubleshooting de Rede

---

### Projetista Eletricista Residencial | Autônomo

**Jan 2018 – Set 2020 (2 anos 9 meses) | Belém, PA | Presencial**

Gestão autônoma de projetos elétricos residenciais, desenvolvendo competências em documentação técnica (AutoCAD), gestão de projetos e autonomia aplicadas posteriormente em infraestrutura de TI e automação.

**Tecnologias:** AutoCAD • Gestão de Projetos • Documentação Técnica

---

### Estagiário de Informática Aplicada | Universidade Federal do Pará

**Mai 2016 – Abr 2018 (2 anos) | Belém, PA | Presencial**

Base técnica fundamental em redes, sistemas Linux/Windows e troubleshooting, desenvolvendo competências em administração de redes LAN/Wi-Fi, diagnóstico de conectividade e suporte a infraestrutura aplicadas ao longo da carreira em TI.

**Tecnologias:** Linux (Ubuntu) • Windows • Redes LAN/Wi-Fi • DNS/DHCP • FTP/Proxy

---

## Home Lab & Aprendizado Contínuo

Mantenho home lab ativo para aprendizado prático e experimentação com tecnologias modernas de SRE, com projetos documentados no GitHub demonstrando aplicação de conceitos:

- **Kubernetes & Orquestração:** Cluster **k3s** de alta disponibilidade em **Proxmox** aplicando práticas **GitOps** e ArgoCD. Deploy de Zabbix usando Terraform + Ansible + Helm (IaC end-to-end). Implementação de ConfigMaps, Secrets e Ingress controllers.
- **Terraform & IaC:** Automação de provisionamento em Proxmox com cloud-init templates, networking (NAT, iptables), e geração dinâmica de inventários Ansible. Módulos reutilizáveis para infraestrutura declarativa.
- **CI/CD Pipelines:** Experimentação com **ArgoCD** para deploys declarativos, **GitHub Actions** para workflows de automação, custom Docker images com multi-stage builds.
- **Cloud Pública:** Estudos e projetos práticos em **AWS** (avançando de Cloud Fundamentals para Cloud Architect). Experiência com AWS Pricing Calculator para dimensionamento de custos.
- **Observabilidade Completa:** Stack LGTM (Loki, Grafana, Tempo, Mimir) com **Grafana Alloy** para telemetria, MinIO para storage de longo prazo.
- **Infrastructure as Code:** Módulos **Terraform** (Proxmox provider), 10+ roles **Ansible** reutilizáveis, scripts de automação.
- **Programação:** Ferramentas CLI em **Python** com design patterns avançados (Singleton, Factory, Async/Await) - grafana-cli-tool, ssh-orchestrator, netbox-zabbix-sync, P2P network monitor com asyncssh. Estudos em **Go**, scripts **Bash**.

---

## Competências Técnicas

### SRE & Observabilidade

**Stack Completa:** Prometheus (Mimir) • Grafana • Loki • Promtail • Zabbix • Elasticsearch • Rsyslog • Node Exporter • fping Exporter (customizado)  
**Práticas:** SLIs • SLOs • SLAs • Error Budget • Golden Signals • RCA • Blameless Post-mortem • MTTD/MTTR  
**Integrações:** NetBox (Source of Truth) • API-driven monitoring

### Infraestrutura & Cloud

**Nuvem Privada:** OpenStack • MinIO • Docker • Docker Compose  
**Sistemas:** Linux (Debian, Ubuntu - administração, hardening, systemd) • Nginx (reverse proxy, SSL/TLS)  
**Orquestração:** Kubernetes (Home Lab - k3s, Proxmox)  
**Cloud Pública:** AWS (Cloud Fundamentals, em estudo para Cloud Architect)

### Automação & IaC

**IaC:** Ansible (10+ roles, 15+ playbooks) • Terraform (Proxmox provider, cloud-init automation)  
**Linguagens:** Python (APIs, CLI tools com design patterns, async programming) • Bash Scripting • Go (em aprendizado)  
**Versionamento:** Git • Gitea

### Banco de Dados

**Administração:** PostgreSQL • MySQL • MariaDB • MongoDB (deploy automatizado via Ansible)  
**Time Series:** Prometheus (Mimir, remote write, capacity planning) • VictoriaMetrics (conhecimento básico)

### CI/CD

**Em Uso:** Jenkins  
**Home Lab:** GitHub Actions • ArgoCD • Git Hooks

### Redes

**FTTH:** Troubleshooting avançado • Diagnóstico de conectividade • DNS/DHCP • QoS/VLANs  
**Equipamentos:** ZTE • FiberHome • TP-Link • Mikrotik  
**Monitoramento:** NETNUMEN • UNM • SNMP

### Segurança

Patches de Segurança • Auditoria de Acessos • Controles de Acesso • Hardening Linux

### Análise de Dados

Power BI • Excel • Python (Pandas, NumPy, Jupyter Notebook)

### Processos & Gestão

**ITSM:** ITIL • GLPI • Wiki.js (administração)  
**Metodologias:** Lean • Kanban • 5 Porquês • Matriz de Prioridade • Análise SWOT  
**Documentação:** C4 Model • AutoCAD

### Soft Skills

Resolução de Problemas • Pensamento Analítico • Autonomia • Aprendizado Rápido • Adaptabilidade • Comunicação Técnica • Trabalho em Equipe • Busca por Melhoria Contínua

---

## Idiomas

- **Inglês:** Fluente (B2/C1) - Leitura, escrita e conversação
- **Português:** Nativo

---

## Certificações Principais

### SRE, Cloud & DevOps (2024-2025)

- **Cloud Basics: Development and Basic Concepts (CRA Training Program)** - Huawei | Ago 2025
- **DevOps: explorando conceitos, comandos e scripts no Linux CLI** - Alura | Jun 2024
- **Formação Começando com Linux** - Alura | Mai 2024
- **Certificação Linux LPI Essentials** (Série completa) - Linux Professional Institute | Jun-Ago 2024

### Liderança Técnica (2023-2025)

- **Formação Tech Lead** - Alura | Abr 2025
- **Mindset digital: técnicas e habilidades para liderança remota** - Alura | Out 2023
- **Hábitos na liderança: boas práticas** - Alura | Mar 2023

### Networking & Infraestrutura (2023)

- **Redes: construindo um projeto com VLANs, políticas de acesso e conexão com internet** - Alura | Ago 2023
- **Redes: dos conceitos iniciais à criação de uma intranet** - Alura | Ago 2023
- **Curso MikroTik para iniciantes** - Redes Brasil | Jul 2023

### Formações Complementares

- **Controle e Automação Industrial** - Estácio | Jun 2024
- **Sistemas e Programação Aplicada a Sistemas Elétricos** - Estácio | Jun 2024
- **Python para Data Science** - Alura | Jun 2022

---

**Lista completa de certificações e credenciais verificáveis disponíveis no LinkedIn**

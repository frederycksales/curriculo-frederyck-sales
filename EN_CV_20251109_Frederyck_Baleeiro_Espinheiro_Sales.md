**Frederyck Baleeiro Espinheiro Sales**

**Site Reliability Engineer (SRE) | Observability Engineer - English Fluent (B2/C1)**  
**(91) 9 9221-2185 • <frederyck.sales@hotmail.com> • [LinkedIn](https://linkedin.com/in/frederyck-baleeiro-espinheiro-sales-4836b4125) • [GitHub](https://github.com/frederycksales) • Castanhal – Pará, Brazil**

---

## Summary

Site Reliability Engineer (SRE) with **7 years in IT** and **2 years specialized in SRE/Observability**, focused on high-performance distributed systems. As **NOC Lead**, I architect and manage the complete monitoring stack (Prometheus, Grafana, Loki, Zabbix, Elasticsearch), delivering **99% availability** and **80%+ reduction in alert noise**. Solid experience in **automation (Ansible, Terraform)**, **IaC**, **GitOps**, and continuous improvement culture based on metrics (SLIs/SLOs).

**Key Results:**

- **80%+ reduction in alert noise** in an environment with **400+ monitored hosts**, through implementation of SLI/SLO-based alerts and Event Management Process.
- **99% availability** of critical monitoring services **supporting 24/7 administrative users**, applying IaC, staging environments, and GitOps.
- **Reduction of critical incidents in monitoring infrastructure** from an average of 2 incidents per month to less than 2 per year, applying automated state compliance assessments and action through playbooks and runbooks.
- **Server provisioning accelerated from hours to minutes** through Ansible automation, increasing operational efficiency and reducing configuration errors.

---

## Education

**Specialization in Site Reliability Engineering (SRE)** | PUC Minas | 2025 – 2026 (In Progress)

**Bachelor's Degree in Electrical Engineering** | Universidade Estácio de Sá | 2020 – 2024 (Completed)  
*Emphasis on Signals and Systems, Statistics, and Computational Modeling. Thesis on Machine Learning applied to electrical systems.*

---

## Professional Experience

### NOC Lead - Observability | Sea Telecom

**Jul 2023 – Present (2 years 4 months) | Castanhal, PA | On-site**

Direct report to NOC management, working autonomously responsible for the architecture, implementation, and operation of the complete monitoring stack and observability culture, managing all related infrastructure.

#### SITE RELIABILITY ENGINEERING (SRE)

**Monitoring & Observability Stack:**

- Architected and implemented complete observability stack: **Prometheus (Mimir as TSDB)**, **Grafana**, **Loki**, **Zabbix**, **Elasticsearch**, and **Rsyslog**.
- Manage all supporting infrastructure: dedicated **PostgreSQL** and **MySQL** databases, **custom exporters** (Node Exporter, internally developed fping-exporter), **Nginx** as reverse proxy.
- **Zabbix Server Performance Tuning:** Optimization of configuration parameters (`zabbix_server.conf`), tuning of internal processes (pollers, trappers, history syncers) and database query optimization to support 400+ hosts with high performance.
- **Prometheus Exporters Development:** Creation of fping-exporter for large-scale network latency metrics.
- Created dashboards focused on **SLIs/SLOs** based on **Golden Signals** (Latency, Traffic, Errors, Saturation), becoming the main tool for decision-making.
- **80%+ reduction in alert noise**, focusing the team on high-impact incidents.
- **40%+ improvement in MTTD** (Mean Time to Detect) for critical incidents.

**Incident Management & Reliability:**

- Conduct **RCA (Root Cause Analysis)** and **Blameless Post-mortems** for continuous learning.
- Implementation of **SLIs, SLOs, and SLAs** to ensure service reliability.
- **Capacity Planning:** Analysis of TSDB growth with usage projection until 2026 using statistical modeling, implementing remote write strategy to Mimir with 80% reduction in local storage.
- **Dashboard Design:** Creation of SLI-oriented dashboards for L1/L2 infrastructure, optimizing incident visibility for NOC in home office model.
- Multi-vendor network observability (Huawei, Datacom, Fiberhome, ZTE) via **SNMP**.
- **Contribution to 99% availability** and reduction of annual critical incidents from 4 to 1.

#### AUTOMATION AND INFRASTRUCTURE AS CODE (IaC)

**Ansible Automation:**

- Developed **automation framework with 10+ reusable roles** (PostgreSQL, MariaDB, MongoDB, Zabbix, GLPI, MinIO) with Jinja2 templates, handlers, and systemd service management.
- Creation of **15+ production playbooks** for deployment, troubleshooting, and automated remediation (fix-readonly-filesystem, diagnose-filesystem, deploy-observability-stack).
- **Server provisioning reduced from hours to minutes**, eliminating 95% of manual configuration errors through structured inventories and state validation.
- Implementation of **IaC** with **Terraform** and **Ansible** for environment versioning and reproducibility.

**Python Tool Development:**

- **NetBox-Zabbix Comparator:** Production CLI tool for inventory auditing between NetBox (Source of Truth) and Zabbix, with discrepancy analysis (IP conflicts, status), ICMP connectivity tests, and executive Excel report export. Layered architecture with 15 decoupled components, build automation (PyInstaller), and code quality (Black, Ruff).
- **CPE Onboarding/Offboarding Automation:** Automation system for CPE lifecycle management between NetBox and Zabbix, with data normalization (DBML schema), compliance validations, operation backup/rollback, and complete traceability via structured logs.
- **Grafana CLI Tool:** Application for dashboard backup management with professional structure (pyproject.toml, automated tests).
- **SSH Orchestrator:** Multi-host command orchestration with structured logging and modular configuration.
- **Backup Automation:** Complete system for Wiki.js (PostgreSQL dump + MinIO upload) with retry logic and notifications.
- **Prometheus Exporters:** Development of custom fping-exporter for network latency metrics.
- **Zabbix Log Analyzer:** Troubleshooting tool for SNMP error analysis with KPI dashboards (Rich library), statistical analysis, and temporal pattern identification.
- Security hardening automation on Linux servers: patch application, access auditing, and control implementation.

**Infrastructure:**

- Complete management of **on-premise infrastructure (OpenStack)**: provisioning, configuration, monitoring, and maintenance of Linux VMs.
- **Service Containerization:** Deployment and orchestration of complex stacks with Docker Compose (LGTM stack, Observability stack with Loki+Mimir+MinIO+Grafana Alloy). Planning migration to Kubernetes in staging environment (ConfigMaps, Secrets, Ingress controllers).
- **Reverse Proxy:** Advanced Nginx configuration for multiple services with SSL/TLS, rate limiting, and load balancing.
- Configuration and script versioning with **Git/Gitea**.
- Administration of **Wiki.js** as central technical documentation platform (including automated backups and disaster recovery).

#### LEADERSHIP AND INNOVATION

- Technical leadership of NOC team in adopting innovation and continuous improvement culture.
- **SRE Technical Proposal:** Development of executive proposal in LaTeX (ABNT standard) with C4 diagrams (PlantUML) for solution architecture, implementation planning, ROI indicators, and SLIs/SLOs/Error Budgets strategy.
- Feasibility studies for migration to public cloud (**AWS**, GCP) and SaaS adoption (Grafana Cloud, Netdata), including cost analysis with AWS Pricing Calculator and TCO (Total Cost of Ownership) comparisons.
- Planning implementation of **ITIL**-based processes with **GLPI**.
- Focus on performance metrics (**MTTD, MTTR**) to guide decision-making.

**Technologies:** Prometheus (Mimir) • Grafana • Loki • Zabbix • Elasticsearch • Rsyslog • OpenStack • Docker • Linux (Debian/Ubuntu) • PostgreSQL • MySQL • Nginx • Python • Ansible • Terraform • Bash • Git/Gitea • GLPI • Wiki.js • Jenkins

---

### Customer Support Lead | Sea Telecom

**Sep 2022 – Jul 2023 (11 months) | Castanhal, PA | On-site**

Technical leadership of support teams, evolving from general management to coordination of specialists focused on critical cases. Fundamental experience for transition to SRE.

**Key Achievements:**

- Acted as central point during **service incidents**, coordinating response and minimizing customer impact.
- Implementation of **KPI**-based data analysis (**Power BI**) to optimize processes, achieving **25% reduction in resolution time**.
- Application of **Lean** and **Kanban** principles to manage demand flow.
- Use of analytical tools (**5 Whys**, **Priority Matrix**, **SWOT Analysis**) to eliminate bottlenecks.

**Technologies:** Power BI • Excel • Lean (Kanban, 5 Whys) • Incident Management • ITIL

---

### Customer Support Assistant | Sea Telecom

**Feb 2022 – Dec 2022 (11 months) | Castanhal, PA | On-site**

Diagnosis and resolution of connectivity issues in FTTH networks, deepening understanding of stability impact on user experience.

**Key Achievements:**

- Customer service data analysis with **Power BI** and **Python** (Pandas, NumPy, Jupyter Notebook) to identify trends and failure patterns.
- Provision of insights for continuous service improvement.
- Technical training for new employees.

**Technologies:** Power BI • Python (Pandas, NumPy, Jupyter Notebook) • FTTH • Troubleshooting

---

### Telemarketing Operator | Sea Telecom

**Sep 2020 – Feb 2022 (1 year 6 months) | Castanhal, PA | On-site**

Technical support for FTTH broadband services, building technical foundation in networking and diagnostics.

**Key Achievements:**

- Network diagnosis: latency analysis, disconnections, DNS, DHCP using Ping, Traceroute, and log analysis.
- Use of NMS: **NETNUMEN (ZTE)** and **UNM (FiberHome)** for device configuration, performance and health analisys.
- Network equipment configuration (ZTE, FiberHome, TP-Link routers): SSID, WPA2, QoS, VLANs.

**Technologies:** FTTH • NETNUMEN/UNM • DNS/DHCP • QoS/VLANs • Network Troubleshooting

---

### Residential Electrical Designer | Freelance

**Jan 2018 – Sep 2020 (2 years 9 months) | Belém, PA | On-site**

Autonomous management of residential electrical projects, developing skills in technical documentation (AutoCAD), project management, and autonomy later applied to IT infrastructure and automation.

**Technologies:** AutoCAD • Project Management • Technical Documentation

---

### IT Intern | Federal University of Pará

**May 2016 – Apr 2018 (2 years) | Belém, PA | On-site**

Fundamental technical foundation in networking, Linux/Windows systems, and troubleshooting, developing skills in LAN/Wi-Fi network administration, connectivity diagnosis, and infrastructure support applied throughout IT career.

**Technologies:** Linux (Ubuntu) • Windows • LAN/Wi-Fi Networks • DNS/DHCP • FTP/Proxy

---

## Home Lab & Continuous Learning

I maintain an active home lab for experimentation and continuous learning, with GitHub repositories demonstrating practical implementations and documented projects:

- **Kubernetes & Orchestration:** High-availability **k3s** cluster on **Proxmox** with **GitOps** practices and ArgoCD. Complete Zabbix deployment using Terraform + Ansible + Helm (end-to-end IaC). Implementation of ConfigMaps, Secrets, and Ingress controllers for configuration management and routing.
- **Terraform & IaC:** Provisioning automation on Proxmox with cloud-init templates, networking (NAT, iptables), and dynamic Ansible inventory generation. Reusable modules for declarative infrastructure.
- **CI/CD Pipelines:** **ArgoCD** for declarative deployments, **GitHub Actions** for automation workflows, custom Docker images with multi-stage builds.
- **Public Cloud:** **AWS** projects and exercises (advancing from Cloud Fundamentals to Cloud Architect). Experience with AWS Pricing Calculator for cost sizing and TCO analysis.
- **Complete Observability:** LGTM stack (Loki, Grafana, Tempo, Mimir) with **Grafana Alloy** for telemetry, MinIO for long-term storage.
- **Infrastructure as Code:** **Terraform** modules (Proxmox provider), 10+ reusable **Ansible** roles, automation scripts.
- **Programming:** CLI tools in **Python** with advanced design patterns (Singleton, Factory, Async/Await) - grafana-cli-tool, ssh-orchestrator, netbox-zabbix-sync, P2P network monitor with asyncssh. Applications in **Go**, **Bash** scripts.

---

## Technical Skills

### SRE & Observability (Production)

**Complete Stack:** Prometheus (Mimir) • Grafana • Loki • Promtail • Zabbix • Elasticsearch • Rsyslog • Node Exporter • fping Exporter (customized)  
**Practices:** SLIs • SLOs • SLAs • Error Budget • Golden Signals • RCA • Blameless Post-mortem • MTTD/MTTR  
**Integrations:** NetBox (Source of Truth) • API-driven monitoring

### Infrastructure & Cloud

**Private Cloud:** OpenStack • MinIO • Docker • Docker Compose  
**Systems:** Linux (Debian, Ubuntu - advanced administration, hardening, systemd) • Nginx (reverse proxy, SSL/TLS)  
**Orchestration:** Kubernetes (Home Lab - k3s, Proxmox)  
**Public Cloud:** AWS (Cloud Fundamentals, studying Cloud Architect)

### Automation & IaC

**IaC:** Ansible (10+ production roles, 15+ playbooks) • Terraform (Proxmox provider, cloud-init automation)  
**Languages:** Python (APIs, CLI tools with design patterns, async programming) • Bash Scripting • Go (in development)  
**Version Control:** Git • Gitea

### Databases

**Administration:** PostgreSQL • MySQL • MariaDB • MongoDB (automated deployment via Ansible)  
**Time Series:** Prometheus (Mimir, remote write, capacity planning) • VictoriaMetrics

### CI/CD

**Production:** Jenkins  
**Home Lab:** GitHub Actions • ArgoCD • Git Hooks

### Networking

**FTTH:** Advanced troubleshooting • Connectivity diagnosis • DNS/DHCP • QoS/VLANs  
**Equipment:** ZTE • FiberHome • TP-Link • Mikrotik  
**Monitoring:** NETNUMEN • UNM • SNMP

### Security

Security Patches • Access Auditing • Access Controls • Linux Hardening

### Data Analysis

Power BI • Excel • Python (Pandas, NumPy, Jupyter Notebook)

### Processes & Management

**ITSM:** ITIL • GLPI • Wiki.js (complete administration)  
**Methodologies:** Lean • Kanban • 5 Whys • Priority Matrix • SWOT Analysis  
**Documentation:** C4 Model • AutoCAD

### Soft Skills

Problem Solving • Analytical Thinking • Autonomy • Continuous Improvement Culture • Technical Communication • Teamwork • Adaptability

---

## Languages

- **English:** Fluent (B2) - Reading, writing, and conversation
- **Portuguese:** Native

---

## Key Certifications

### SRE, Cloud & DevOps (2024-2025)

- **Cloud Basics: Development and Basic Concepts (CRA Training Program)** - Huawei | Aug 2025
- **DevOps: exploring concepts, commands and scripts in Linux CLI** - Alura | Jun 2024
- **Getting Started with Linux Track** - Alura | May 2024
- **Linux LPI Essentials Certification** (Complete Series) - Linux Professional Institute | Jun-Aug 2024

### Technical Leadership (2023-2025)

- **Tech Lead Track** - Alura | Apr 2025
- **Digital mindset: techniques and skills for remote leadership** - Alura | Oct 2023
- **Leadership habits: best practices** - Alura | Mar 2023

### Networking & Infrastructure (2023)

- **Networks: building a project with VLANs, access policies and internet connection** - Alura | Aug 2023
- **Networks: from initial concepts to intranet creation** - Alura | Aug 2023
- **MikroTik Course for Beginners** - Redes Brasil | Jul 2023

### Complementary Training

- **Industrial Control and Automation** - Estácio | Jun 2024
- **Systems and Programming Applied to Electrical Systems** - Estácio | Jun 2024
- **Python for Data Science** - Alura | Jun 2022

---

**Complete list of certifications and verifiable credentials available on LinkedIn**

import os
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

SERVICES = [
    ('identity-access-management', 'Identity & Access Management', 'Robust frameworks to ensure the right people access the right resources at the right time.', 'Identity and Access Management (IAM) delivers secure authentication, authorization, and privileged access controls that keep modern enterprise environments protected.', [
        ('Role-Based Access Control', 'Fine-grained permissions aligned to user roles and enterprise policy.'),
        ('Multi-Factor Authentication', 'Strong authentication across systems for every user and device.'),
        ('Single Sign-On', 'Streamlined access with centralized login and secure federation.'),
        ('Privileged Access Governance', 'Control and audit administrative access with policy enforcement.'),
    ]),
    ('data-protection-privacy', 'Data Protection & Privacy', 'End-to-end safeguards to keep your sensitive data secure and your business compliant.', 'Modern data protection and privacy controls help enterprises secure regulated data, reduce breach risk, and meet global compliance requirements.', [
        ('Data Encryption', 'Encrypting data in transit and at rest to protect critical information.'),
        ('Data Loss Prevention', 'Preventing accidental or malicious data exposure across systems.'),
        ('Privacy by Design', 'Embedding privacy controls into applications and infrastructure.'),
        ('Compliance Reporting', 'Automated evidence and controls for GDPR, CCPA, and other standards.'),
    ]),
    ('vulnerability-management', 'Vulnerability Management', 'Proactive identification and remediation of weaknesses before attackers exploit them.', 'Vulnerability management keeps systems hardened and reduces risk through continuous discovery, prioritization, and remediation workflows.', [
        ('Continuous Scanning', 'Automated scans across networks, applications, and endpoints.'),
        ('Risk Prioritization', 'Prioritize remediation where business risk is highest.'),
        ('Patch Management', 'Fast patching and configuration hardening to close exposure windows.'),
        ('Threat Validation', 'Confirm vulnerability impact with real-world testing scenarios.'),
    ]),
    ('managed-security-services', 'Managed Security Services', 'Always-on security operations so your team can focus on the business.', 'Managed Security Services deliver a persistent security operations center, incident response, and expert threat management as an outsourced capability.', [
        ('24/7 Monitoring', 'Security operations that detect and escalate incidents around the clock.'),
        ('Threat Detection', 'Context-aware analytics identifying suspicious activity in real time.'),
        ('Incident Response', 'Rapid containment and recovery when threats are detected.'),
        ('Security Reporting', 'Actionable dashboards and compliance-ready reports for stakeholders.'),
    ]),
    ('cyber-ai-solutions', 'Cyber AI Solutions', 'AI and machine learning that predict, detect, and neutralize sophisticated threats automatically.', 'AI-driven security analyzes behavior, uncovers hidden threats, and helps your teams respond with speed and precision.', [
        ('Predictive Attacks', 'Forecast when and where adversaries are likely to strike.'),
        ('Behavioral Analytics', 'Detect anomalous activity using machine learning models.'),
        ('Automated Response', 'Trigger containment actions without human delay.'),
        ('Threat Scoring', 'Rank incidents by risk to focus response on the biggest threats.'),
    ]),
    ('infrastructure-security', 'Infrastructure Security', 'Hardening every layer of your physical and virtual environment.', 'Infrastructure security protects the foundation of your enterprise, including networks, servers, clouds, and critical operational systems.', [
        ('Network Segmentation', 'Reducing attack paths with micro-segmentation and zoning.'),
        ('Endpoint Protection', 'Protecting devices with modern EDR and behavioral defenses.'),
        ('Cloud Workload Security', 'Security controls for containers, VMs, and serverless assets.'),
        ('Infrastructure Monitoring', 'Visibility into changes, configuration drift, and vulnerabilities.'),
    ]),
    ('operational-technology-security', 'Operational Technology (OT) Security', 'Specialized protection for industrial environments where uptime is mission-critical.', 'OT security safeguards production systems, control networks, and industrial equipment with targeted controls that minimize disruption.', [
        ('ICS Protection', 'Shielding industrial control systems from cyber threats.'),
        ('SCADA Monitoring', 'Continuous visibility into industrial systems and sensors.'),
        ('Segmentation Controls', 'Separating OT networks from IT to reduce attack surface.'),
        ('Safety & Compliance', 'Maintaining operational integrity alongside regulatory requirements.'),
    ]),
    ('threat-detection-response', 'Threat Detection & Response', 'Advanced detection and rapid response to contain threats before they escalate.', 'Threat detection and response helps organizations identify breaches faster and neutralize threats with coordinated actions.', [
        ('Threat Hunting', 'Proactive searches for hidden adversary activity in your environment.'),
        ('Security Orchestration', 'Coordinated responses across tools and teams to reduce dwell time.'),
        ('Alert Triage', 'Filtering noise to focus analysts on true incidents.'),
        ('Containment Playbooks', 'Repeatable response procedures for rapid mitigation.'),
    ]),
    ('governance-risk-compliance', 'Governance, Risk & Compliance', 'Aligning your IT security posture with business strategy and regulatory expectations.', 'GRC consulting helps enterprises translate requirements into controls, policies, and measurable risk programs.', [
        ('Policy Frameworks', 'Documented security policies aligned to best practices.'),
        ('Risk Assessments', 'Enterprise risk evaluations that support better decisions.'),
        ('Control Maturity', 'Improving security program maturity with measured outcomes.'),
        ('Audit Readiness', 'Preparing teams for internal and external compliance reviews.'),
    ]),
    ('cloud-security', 'Cloud Security', 'Consistent, scalable security across AWS, Azure, GCP, and hybrid environments.', 'Cloud security protects workloads, data, and identities in modern multi-cloud infrastructures with policy, automation, and monitoring.', [
        ('Cloud Posture Management', 'Continuous compliance and misconfiguration remediation.'),
        ('Identity Security', 'Protecting cloud identities and access across accounts.'),
        ('Workload Defense', 'Security controls for containers, VMs, and serverless functions.'),
        ('Encrypted Data Services', 'Strong encryption for cloud storage and messaging services.'),
    ]),
    ('cyber-advisory-services', 'Cyber Advisory Services', 'Strategic guidance that strengthens your risk posture and security program.', 'Advisory services provide expert planning, maturity assessment, and security program design tailored to your organization.', [
        ('Maturity Assessments', 'Benchmarking your security program against industry standards.'),
        ('Roadmap Development', 'Actionable security roadmaps for near-term and long-term goals.'),
        ('Executive Briefings', 'Clear risk communication for leadership and boards.'),
        ('Program Governance', 'Oversight structures for sustained security operations.'),
    ]),
    ('sase', 'SASE', 'Secure access for distributed teams with identity-aware networking and cloud-delivered protection.', 'Secure Access Service Edge merges networking and security in the cloud to support remote work and hybrid infrastructure securely.', [
        ('Zero Trust Access', 'Identity-first access controls for distributed applications.'),
        ('Cloud Firewall', 'Traffic filtering and policy enforcement at the cloud edge.'),
        ('Secure Web Gateway', 'Protecting web traffic from threats and data leakage.'),
        ('SD-WAN Integration', 'Performance-aware networking for branch and remote connectivity.'),
    ]),
    ('hybrid-cloud-security', 'Hybrid Cloud Security', 'Unified protection for applications and data across on-premises and public cloud.', 'Hybrid cloud security ensures consistent controls for workloads that span datacenters and cloud providers.', [
        ('Unified Policy', 'Single security policy enforcement across environments.'),
        ('Secure Connectivity', 'Encrypted links and trusted tunnels between sites and clouds.'),
        ('Visibility & Analytics', 'Cross-environment insights into security events and compliance.'),
        ('Hybrid Identity', 'Consistent identity controls across on-prem and cloud.'),
    ]),
    ('custom-software-development', 'Custom Software Development', 'Tailored solutions engineered to fit your specific business workflows and user needs.', 'Bespoke software development that solves unique enterprise problems with quality, agility, and long-term maintainability.', [
        ('Solution Architecture', 'Designing systems around your business operations and growth plans.'),
        ('Product Engineering', 'Building user-focused web, mobile, and cloud applications.'),
        ('Integration Services', 'Connecting systems, APIs, and data sources reliably.'),
        ('Maintenance & Support', 'Ongoing updates and application support after launch.'),
    ]),
    ('full-stack-development', 'Full-Stack Development', 'Comprehensive ownership of your entire technology stack, from UI to database to deployment.', 'Full-stack development teams deliver cohesive solutions across frontend, backend, and deployment pipelines.', [
        ('Frontend Engineering', 'Modern web experiences built for performance and accessibility.'),
        ('Backend Services', 'Robust API and service layers that scale with demand.'),
        ('Data Modeling', 'Well-structured data layers to support reliable operations.'),
        ('DevOps Automation', 'CI/CD and infrastructure automation for faster delivery.'),
    ]),
    ('legacy-system-modernization', 'Legacy System Modernization', 'Transforming outdated technology into competitive, maintainable modern systems.', 'Modernization programs reduce technical debt and enable enterprise agility for long-running systems.', [
        ('Application Refactoring', 'Rewriting or reorganizing legacy code into modern architecture.'),
        ('Platform Migration', 'Moving legacy systems onto cloud-native infrastructure.'),
        ('Data Modernization', 'Converting legacy data stores to contemporary platforms.'),
        ('Incremental Modernization', 'Reducing risk with phased migrations and parallel operations.'),
    ]),
    ('cloud-native-development', 'Cloud-Native Development', 'Applications built from the ground up to leverage the full power of cloud platforms.', 'Cloud-native development accelerates innovation with microservices, containers, and serverless design patterns.', [
        ('Container Strategy', 'Deploying applications as modular, portable containers.'),
        ('Serverless Functions', 'On-demand compute that scales with real usage.'),
        ('Service Mesh', 'Secure service communication for distributed applications.'),
        ('Cloud Automation', 'Infrastructure as code and platform automation for repeatability.'),
    ]),
    ('qa-automated-testing', 'QA & Automated Testing', 'Rigorous quality assurance that catches defects early and builds confidence at every release.', 'Automated testing ensures software quality and reliability across every stage of the development lifecycle.', [
        ('Test Automation', 'Automated regression and end-to-end testing frameworks.'),
        ('Performance Testing', 'Load and stress testing to avoid production failures.'),
        ('Security Testing', 'Integrating SAST, DAST, and compliance scans into release cycles.'),
        ('Quality Engineering', 'Proactive quality processes that reduce rework and defects.'),
    ]),
    ('intelligent-automation', 'Intelligent Automation', 'Combining AI with process automation to eliminate repetitive work and accelerate business operations.', 'Intelligent automation reduces costs and boosts throughput by automating repeatable, rules-based business processes.', [
        ('Robotic Process Automation', 'Bots that execute high-volume processes with precision.'),
        ('Workflow Orchestration', 'Automated coordination of business processes and handoffs.'),
        ('AI Decision Support', 'Embedding intelligence into operational decisions.'),
        ('Service Automation', 'Self-service automation for employees and customers.'),
    ]),
    ('machine-learning-solutions', 'Machine Learning Solutions', 'Custom ML models that turn your data into competitive advantage through prediction and insight.', 'Machine learning helps enterprises anticipate outcomes, improve decisions, and unlock new business value.', [
        ('Predictive Analytics', 'Forecasting demand, risk, and customer behavior.'),
        ('Recommendation Engines', 'Personalized experiences that increase engagement.'),
        ('Text & Vision AI', 'NLP and computer vision for unstructured data problems.'),
        ('Model Deployment', 'Production-ready ML workflows with ongoing monitoring.'),
    ]),
    ('ai-agent-development', 'AI Agent Development', 'Building autonomous systems that reason, plan, and act on behalf of your organization.', 'AI agents automate decision-making and coordination across workflows for scalable enterprise intelligence.', [
        ('Autonomous Agents', 'AI systems that execute tasks with minimal human supervision.'),
        ('Multi-Agent Coordination', 'Collaborating agents that solve complex, distributed problems.'),
        ('Agent Orchestration', 'Managing agent workflows and approvals safely.'),
        ('Decision Automation', 'Turning business logic into repeatable, rule-based actions.'),
    ]),
    ('genai-solutions', 'GenAI Solutions', 'Harnessing the power of large language models to transform enterprise content, code, and workflows.', 'Generative AI accelerates content creation, knowledge discovery, and productivity for enterprise teams.', [
        ('Custom Prompt Design', 'Tailored prompts and templates for business outcomes.'),
        ('Content Automation', 'AI-generated content for marketing, documentation, and operations.'),
        ('Conversational Assistants', 'Chat-driven workflows for support and productivity.'),
        ('Code Intelligence', 'AI-assisted development, review, and code generation.'),
    ]),
    ('data-engineering-ai', 'Data Engineering for AI', 'Building the data foundation that makes your AI systems reliable, scalable, and production-ready.', 'Data engineering creates the pipelines and models enterprises need for trusted AI outcomes.', [
        ('Data Pipelines', 'Reliable ingestion, transformation, and delivery of enterprise data.'),
        ('Feature Stores', 'Structured data layers that power consistent machine learning.'),
        ('Data Quality', 'Validation, cleansing, and governance for AI-ready data.'),
        ('MLOps Support', 'Operational workflows for model deployment and monitoring.'),
    ]),
    ('it-infrastructure', 'IT Infrastructure', 'Designing, migrating, and managing the technology foundations your business runs on.', 'IT infrastructure services ensure your systems are stable, scalable, and ready for digital growth.', [
        ('Cloud Migrations', 'Moving applications and workloads to modern cloud platforms.'),
        ('Network Architecture', 'Designing resilient and high-performance network topologies.'),
        ('Virtualization', 'Optimizing compute utilization with virtualized environments.'),
        ('Infrastructure Monitoring', 'Continuous visibility into availability and performance.'),
    ]),
    ('managed-services', 'Managed Services', 'Comprehensive, proactive management of your IT environment so your team stays focused on growth.', 'Managed services provide continuous support, monitoring, and optimization for your IT operations.', [
        ('24/7 Support', 'Dedicated technical support for your team and systems.'),
        ('Infrastructure Management', 'Proactive maintenance and platform upkeep.'),
        ('Cost Optimization', 'Managing resources to reduce spend and increase efficiency.'),
        ('Service Desk Operations', 'User support and incident management across the enterprise.'),
    ]),
    ('enterprise-solutions', 'Enterprise Solutions', 'Implementing and optimizing the enterprise platforms that run your core business processes.', 'Enterprise solutions bring together ERP, CRM, and analytics systems that support large-scale operational workflows.', [
        ('ERP Deployments', 'Enterprise resource planning platforms for finance and operations.'),
        ('CRM Implementations', 'Customer relationship platforms aligned with sales and service.'),
        ('Analytics Platforms', 'Reporting systems that turn operational data into insight.'),
        ('Integration Services', 'Connecting enterprise systems for data flow and automation.'),
    ]),
    ('digital-transformation', 'Digital Transformation', 'Strategic guidance and execution to modernize your business for the digital era.', 'Digital transformation programs help enterprises reshape processes, technology, and customer experiences.', [
        ('Strategic Roadmaps', 'Clear transformation plans aligned to business goals.'),
        ('Change Management', 'Supporting teams as new technologies and processes are adopted.'),
        ('Process Optimization', 'Efficiency improvements across operations and services.'),
        ('Capability Uplift', 'Training and enablement for new digital skills.'),
    ]),
    ('it-operations', 'IT Operations', 'Day-to-day operational excellence keeping your systems healthy, available, and performing.', 'IT operations services keep your infrastructure reliable with continuous monitoring, recovery, and support.', [
        ('Service Management', 'Structured ITIL-inspired practices for service delivery.'),
        ('Backup & Recovery', 'Reliable backup strategies and disaster recovery plans.'),
        ('Capacity Planning', 'Ensuring systems scale effectively as demand grows.'),
        ('Performance Tuning', 'Optimizing systems for consistent availability.'),
    ]),
]

FAQS = [
    ('How does Softwaresphere ensure a secure implementation for my service?', 'Our teams combine security standards, threat modeling, and continuous validation throughout design, development, and deployment so every service is hardened from day one.'),
    ('Can I engage Softwaresphere for a hybrid implementation across cloud and on-premises systems?', 'Yes. We design hybrid architectures that maintain consistent security, performance, and operational control across cloud providers and data center environments.'),
    ('How quickly can I start a managed services engagement?', 'We typically begin with a discovery and onboarding phase, enabling core monitoring and support within 4–6 weeks depending on your environment and priorities.'),
    ('What makes your AI solutions enterprise-grade?', 'Our AI solutions are built with production-ready data engineering, model governance, explainability, and integration patterns that are designed for enterprise reliability.'),
    ('How does Softwaresphere support compliance requirements?', 'We align our services to applicable standards, provide audit-ready evidence, and integrate compliance controls directly into process and technology implementations.'),
    ('How do you measure success for a service delivery?', 'Success is measured by reduced risk, improved performance, higher automation velocity, and stakeholder adoption across the business.'),
]

INDUSTRIES = [
    'Healthcare',
    'Retail',
    'Manufacturing',
    'Banking',
    'Education',
    'Logistics',
]

ROOT_NAV = '''<nav class="navbar">
  <div class="nav-logo">
    <img src="../images/logo.png" alt="Softwaresphere Logo"/>
    <div class="nav-logo-text">SOFTWARESPHERE<span>SOFTWARE SOLUTIONS</span></div>
  </div>
  <ul class="nav-links">
    <li><a href="../index.html">Home</a></li>
    <li class="nav-item has-mega"><a href="../services/index.html" class="mega-toggle">Services</a></li>
    <li><a href="../cybersecurity.html">Cyber Security</a></li>
    <li><a href="../software.html">Software Dev</a></li>
    <li><a href="../ai-solutions.html">AI Solutions</a></li>
    <li><a href="../it-solutions.html">IT Services</a></li>
    <li><a href="../contact.html" class="nav-cta">Contact Us</a></li>
  </ul>
  <button class="hamburger" aria-label="Menu">
    <span></span><span></span><span></span>
  </button>
</nav>
<nav class="mobile-nav">
  <a href="../index.html">Home</a>
  <button class="accordion-button" type="button">Cyber Security</button>
  <div class="accordion-panel">
    <a href="identity-access-management/index.html">Identity & Access Management</a>
    <a href="data-protection-privacy/index.html">Data Protection & Privacy</a>
    <a href="vulnerability-management/index.html">Vulnerability Management</a>
    <a href="managed-security-services/index.html">Managed Security Services</a>
    <a href="cyber-ai-solutions/index.html">Cyber AI Solutions</a>
    <a href="infrastructure-security/index.html">Infrastructure Security</a>
    <a href="operational-technology-security/index.html">Operational Technology Security</a>
    <a href="threat-detection-response/index.html">Threat Detection & Response</a>
    <a href="governance-risk-compliance/index.html">Governance, Risk & Compliance</a>
    <a href="cloud-security/index.html">Cloud Security</a>
    <a href="cyber-advisory-services/index.html">Cyber Advisory Services</a>
    <a href="sase/index.html">SASE</a>
    <a href="hybrid-cloud-security/index.html">Hybrid Cloud Security</a>
  </div>
  <button class="accordion-button" type="button">Software Development</button>
  <div class="accordion-panel">
    <a href="custom-software-development/index.html">Custom Software Development</a>
    <a href="full-stack-development/index.html">Full-Stack Development</a>
    <a href="legacy-system-modernization/index.html">Legacy System Modernization</a>
    <a href="cloud-native-development/index.html">Cloud-Native Development</a>
    <a href="qa-automated-testing/index.html">QA & Automated Testing</a>
  </div>
  <button class="accordion-button" type="button">AI Solutions</button>
  <div class="accordion-panel">
    <a href="intelligent-automation/index.html">Intelligent Automation</a>
    <a href="machine-learning-solutions/index.html">Machine Learning Solutions</a>
    <a href="ai-agent-development/index.html">AI Agent Development</a>
    <a href="genai-solutions/index.html">GenAI Solutions</a>
    <a href="data-engineering-ai/index.html">Data Engineering for AI</a>
  </div>
  <button class="accordion-button" type="button">IT Services</button>
  <div class="accordion-panel">
    <a href="it-infrastructure/index.html">IT Infrastructure</a>
    <a href="managed-services/index.html">Managed Services</a>
    <a href="enterprise-solutions/index.html">Enterprise Solutions</a>
    <a href="digital-transformation/index.html">Digital Transformation</a>
    <a href="it-operations/index.html">IT Operations</a>
  </div>
  <a href="../cybersecurity.html">Cyber Security</a>
  <a href="../software.html">Software Dev</a>
  <a href="../ai-solutions.html">AI Solutions</a>
  <a href="../it-solutions.html">IT Services</a>
  <a href="../contact.html">Contact Us</a>
</nav>
'''

MEGA_MENU = '''<div class="mega-menu" id="megaMenu">
  <div class="mega-grid">
    <div class="mega-card">
      <div class="mega-icon">🔐</div>
      <h3>Cyber Security Services</h3>
      <p>Protect enterprise assets and strengthen security posture across cloud, OT, and identity domains.</p>
      <ul>
        <li><a href="identity-access-management/index.html">Identity & Access Management</a></li>
        <li><a href="data-protection-privacy/index.html">Data Protection & Privacy</a></li>
        <li><a href="vulnerability-management/index.html">Vulnerability Management</a></li>
        <li><a href="managed-security-services/index.html">Managed Security Services</a></li>
        <li><a href="cyber-ai-solutions/index.html">Cyber AI Solutions</a></li>
        <li><a href="infrastructure-security/index.html">Infrastructure Security</a></li>
        <li><a href="operational-technology-security/index.html">Operational Technology Security</a></li>
        <li><a href="threat-detection-response/index.html">Threat Detection & Response</a></li>
        <li><a href="governance-risk-compliance/index.html">Governance, Risk & Compliance</a></li>
        <li><a href="cloud-security/index.html">Cloud Security</a></li>
        <li><a href="cyber-advisory-services/index.html">Cyber Advisory Services</a></li>
        <li><a href="sase/index.html">SASE</a></li>
        <li><a href="hybrid-cloud-security/index.html">Hybrid Cloud Security</a></li>
      </ul>
    </div>
    <div class="mega-card">
      <div class="mega-icon">💻</div>
      <h3>Software Development & Modernization</h3>
      <p>Build scalable applications, modernize legacy systems and accelerate business transformation.</p>
      <ul>
        <li><a href="custom-software-development/index.html">Custom Software Development</a></li>
        <li><a href="full-stack-development/index.html">Full-Stack Development</a></li>
        <li><a href="legacy-system-modernization/index.html">Legacy System Modernization</a></li>
        <li><a href="cloud-native-development/index.html">Cloud-Native Development</a></li>
        <li><a href="qa-automated-testing/index.html">QA & Automated Testing</a></li>
      </ul>
    </div>
    <div class="mega-card">
      <div class="mega-icon">🤖</div>
      <h3>AI Agents & Intelligent Solutions</h3>
      <p>Empower teams with autonomous intelligence, predictive analytics, and GenAI innovation.</p>
      <ul>
        <li><a href="intelligent-automation/index.html">Intelligent Automation</a></li>
        <li><a href="machine-learning-solutions/index.html">Machine Learning Solutions</a></li>
        <li><a href="ai-agent-development/index.html">AI Agent Development</a></li>
        <li><a href="genai-solutions/index.html">GenAI Solutions</a></li>
        <li><a href="data-engineering-ai/index.html">Data Engineering for AI</a></li>
      </ul>
    </div>
    <div class="mega-card">
      <div class="mega-icon">🖥️</div>
      <h3>IT Solutions & Managed Services</h3>
      <p>Ensure operational excellence with infrastructure management, enterprise systems, and service delivery.</p>
      <ul>
        <li><a href="it-infrastructure/index.html">IT Infrastructure</a></li>
        <li><a href="managed-services/index.html">Managed Services</a></li>
        <li><a href="enterprise-solutions/index.html">Enterprise Solutions</a></li>
        <li><a href="digital-transformation/index.html">Digital Transformation</a></li>
        <li><a href="it-operations/index.html">IT Operations</a></li>
      </ul>
    </div>
  </div>
</div>'''

SERVICES_INDEX_CONTENT = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Services – Softwaresphere Enterprise Services</title>
<meta name="description" content="Softwaresphere enterprise services hub for cybersecurity, software engineering, AI solutions, and IT managed services."/>
<link rel="stylesheet" href="../css/style.css"/>
<link rel="stylesheet" href="../css/services.css"/>
<link rel="icon" href="../images/logo.png"/>
</head>
<body>
<nav class="navbar">
  <div class="nav-logo">
    <img src="../images/logo.png" alt="Softwaresphere Logo"/>
    <div class="nav-logo-text">SOFTWARESPHERE<span>SOFTWARE SOLUTIONS</span></div>
  </div>
  <ul class="nav-links">
    <li><a href="../index.html">Home</a></li>
    <li class="nav-item has-mega"><a href="index.html" class="active mega-toggle">Services</a></li>
    <li><a href="../cybersecurity.html">Cyber Security</a></li>
    <li><a href="../software.html">Software Dev</a></li>
    <li><a href="../ai-solutions.html">AI Solutions</a></li>
    <li><a href="../it-solutions.html">IT Services</a></li>
    <li><a href="../contact.html" class="nav-cta">Contact Us</a></li>
  </ul>
  <button class="hamburger" aria-label="Menu">
    <span></span><span></span><span></span>
  </button>
</nav>
<nav class="mobile-nav">
  <a href="../index.html">Home</a>
  <button class="accordion-button" type="button">Cyber Security</button>
  <div class="accordion-panel">
    <a href="identity-access-management/index.html">Identity & Access Management</a>
    <a href="data-protection-privacy/index.html">Data Protection & Privacy</a>
    <a href="vulnerability-management/index.html">Vulnerability Management</a>
    <a href="managed-security-services/index.html">Managed Security Services</a>
    <a href="cyber-ai-solutions/index.html">Cyber AI Solutions</a>
    <a href="infrastructure-security/index.html">Infrastructure Security</a>
    <a href="operational-technology-security/index.html">Operational Technology Security</a>
    <a href="threat-detection-response/index.html">Threat Detection & Response</a>
    <a href="governance-risk-compliance/index.html">Governance, Risk & Compliance</a>
    <a href="cloud-security/index.html">Cloud Security</a>
    <a href="cyber-advisory-services/index.html">Cyber Advisory Services</a>
    <a href="sase/index.html">SASE</a>
    <a href="hybrid-cloud-security/index.html">Hybrid Cloud Security</a>
  </div>
  <button class="accordion-button" type="button">Software Development</button>
  <div class="accordion-panel">
    <a href="custom-software-development/index.html">Custom Software Development</a>
    <a href="full-stack-development/index.html">Full-Stack Development</a>
    <a href="legacy-system-modernization/index.html">Legacy System Modernization</a>
    <a href="cloud-native-development/index.html">Cloud-Native Development</a>
    <a href="qa-automated-testing/index.html">QA & Automated Testing</a>
  </div>
  <button class="accordion-button" type="button">AI Solutions</button>
  <div class="accordion-panel">
    <a href="intelligent-automation/index.html">Intelligent Automation</a>
    <a href="machine-learning-solutions/index.html">Machine Learning Solutions</a>
    <a href="ai-agent-development/index.html">AI Agent Development</a>
    <a href="genai-solutions/index.html">GenAI Solutions</a>
    <a href="data-engineering-ai/index.html">Data Engineering for AI</a>
  </div>
  <button class="accordion-button" type="button">IT Services</button>
  <div class="accordion-panel">
    <a href="it-infrastructure/index.html">IT Infrastructure</a>
    <a href="managed-services/index.html">Managed Services</a>
    <a href="enterprise-solutions/index.html">Enterprise Solutions</a>
    <a href="digital-transformation/index.html">Digital Transformation</a>
    <a href="it-operations/index.html">IT Operations</a>
  </div>
  <a href="../cybersecurity.html">Cyber Security</a>
  <a href="../software.html">Software Dev</a>
  <a href="../ai-solutions.html">AI Solutions</a>
  <a href="../it-solutions.html">IT Services</a>
  <a href="../contact.html">Contact Us</a>
</nav>
''' + MEGA_MENU + '''
<section class="page-hero">
  <div class="page-hero-label">// ENTERPRISE SERVICES HUB</div>
  <h1>Enterprise Services Designed for Scale, Security, and Speed</h1>
  <p>Discover the four core service categories that bring technology, data, and operations together for sustainable business growth.</p>
  <div class="breadcrumb"><a href="../index.html">Home</a><span>/</span><span>Services Hub</span></div>
</section>
<section class="section" style="background: #FFFFFF;">
  <div class="section-inner">
    <div class="section-label">// CYBER SECURITY SERVICES</div>
    <h2 class="section-title">Protect enterprise assets, ensure compliance, and mitigate digital risks.</h2>
    <div class="section-desc">Security services designed for cloud, hybrid, operational technology, and modern identity environments.</div>
    <div class="services-grid" style="margin-top:2rem;">
      <div class="service-card"><div class="card-icon">🔐</div><div class="card-title">Identity & Access Management</div><p class="card-desc">Strengthen authentication, authorization and privileged access for your enterprise identity ecosystem.</p><a class="card-link" href="identity-access-management/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">🔒</div><div class="card-title">Data Protection & Privacy</div><p class="card-desc">Protect sensitive information and meet privacy requirements with modern data controls.</p><a class="card-link" href="data-protection-privacy/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">🔍</div><div class="card-title">Vulnerability Management</div><p class="card-desc">Identify and remediate weaknesses proactively across applications, endpoints, and networks.</p><a class="card-link" href="vulnerability-management/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">🛡️</div><div class="card-title">Managed Security Services</div><p class="card-desc">Leverage an expert security operations team for continuous protection and response.</p><a class="card-link" href="managed-security-services/index.html">Learn More →</a></div>
    </div>
  </div>
</section>
<section class="section" style="background: #F8FAFC;">
  <div class="section-inner">
    <div class="section-label">// SOFTWARE DEVELOPMENT & MODERNIZATION</div>
    <h2 class="section-title">Build scalable applications and modernize legacy systems.</h2>
    <div class="section-desc">Modern engineering and application transformation services for enterprise digital products.</div>
    <div class="services-grid" style="margin-top:2rem;">
      <div class="service-card"><div class="card-icon">💻</div><div class="card-title">Custom Software Development</div><p class="card-desc">Tailored applications that fit unique enterprise processes and customer experiences.</p><a class="card-link" href="custom-software-development/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">🔗</div><div class="card-title">Full-Stack Development</div><p class="card-desc">Unified frontend, backend, and deployment practices for resilient software delivery.</p><a class="card-link" href="full-stack-development/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">🔄</div><div class="card-title">Legacy System Modernization</div><p class="card-desc">Refresh legacy platforms with modern architecture, migration, and integration services.</p><a class="card-link" href="legacy-system-modernization/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">☁️</div><div class="card-title">Cloud-Native Development</div><p class="card-desc">Build cloud-first applications that scale efficiently and support rapid innovation.</p><a class="card-link" href="cloud-native-development/index.html">Learn More →</a></div>
    </div>
  </div>
</section>
<section class="section" style="background: #FFFFFF;">
  <div class="section-inner">
    <div class="section-label">// AI AGENTS & INTELLIGENT SOLUTIONS</div>
    <h2 class="section-title">Empower businesses with autonomous intelligence.</h2>
    <div class="section-desc">AI systems, predictive analytics, and automation solutions built for enterprise operations.</div>
    <div class="services-grid" style="margin-top:2rem;">
      <div class="service-card"><div class="card-icon">⚡</div><div class="card-title">Intelligent Automation</div><p class="card-desc">Automate rule-based work with AI-enabled orchestration and robotics.</p><a class="card-link" href="intelligent-automation/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">📊</div><div class="card-title">Machine Learning Solutions</div><p class="card-desc">Predict trends and optimize operations with custom machine learning models.</p><a class="card-link" href="machine-learning-solutions/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">🤖</div><div class="card-title">AI Agent Development</div><p class="card-desc">Deploy autonomous agents that coordinate processes and accelerate decision-making.</p><a class="card-link" href="ai-agent-development/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">✨</div><div class="card-title">GenAI Solutions</div><p class="card-desc">Leverage large language models for content, code, and workflow automation.</p><a class="card-link" href="genai-solutions/index.html">Learn More →</a></div>
    </div>
  </div>
</section>
<section class="section" style="background: #F8FAFC; padding-bottom:6rem;">
  <div class="section-inner">
    <div class="section-label">// IT SOLUTIONS & MANAGED SERVICES</div>
    <h2 class="section-title">Ensure operational excellence and business continuity.</h2>
    <div class="section-desc">Managed operations, IT infrastructure, and enterprise systems built for reliability.</div>
    <div class="services-grid" style="margin-top:2rem;">
      <div class="service-card"><div class="card-icon">🏗️</div><div class="card-title">IT Infrastructure</div><p class="card-desc">Design, migrate, and manage the infrastructure that supports your business.</p><a class="card-link" href="it-infrastructure/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">🔧</div><div class="card-title">Managed Services</div><p class="card-desc">Proactive monitoring, support, and operations for your IT environment.</p><a class="card-link" href="managed-services/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">🏢</div><div class="card-title">Enterprise Solutions</div><p class="card-desc">Implement enterprise systems and integrations that support large-scale processes.</p><a class="card-link" href="enterprise-solutions/index.html">Learn More →</a></div>
      <div class="service-card"><div class="card-icon">🚀</div><div class="card-title">Digital Transformation</div><p class="card-desc">Strategic transformation services that modernize your business for growth.</p><a class="card-link" href="digital-transformation/index.html">Learn More →</a></div>
    </div>
  </div>
</section>
<section class="section" style="padding:4rem 2rem; text-align:center; background:#FFFFFF; border-top:1px solid var(--border);">
  <div class="section-inner">
    <div class="section-label">// NEXT STEPS</div>
    <h2 class="section-title">Ready to discuss your enterprise technology roadmap?</h2>
    <p class="section-desc">Contact our team for a service consultation, capability assessment, or implementation plan.</p>
    <div class="hero-btns" style="justify-content:center; margin-top:1.75rem; gap:1rem; flex-wrap:wrap;">
      <a href="../contact.html" class="btn btn-primary">Contact Us</a>
      <a href="../contact.html" class="btn btn-outline">Book a Free Consultation</a>
    </div>
  </div>
</section>
<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="footer-logo"><img src="../images/logo.png" alt="Softwaresphere"/><div class="footer-logo-text">SOFTWARESPHERE</div></div>
        <p>Enterprise-grade technology services for secure, modern, and data-driven businesses.</p>
      </div>
      <div class="footer-col"><h4>Services</h4><ul>
        <li><a href="identity-access-management/index.html">Identity & Access Management</a></li>
        <li><a href="custom-software-development/index.html">Custom Software Development</a></li>
        <li><a href="intelligent-automation/index.html">Intelligent Automation</a></li>
        <li><a href="it-infrastructure/index.html">IT Infrastructure</a></li>
      </ul></div>
      <div class="footer-col"><h4>Company</h4><ul>
        <li><a href="../contact.html">Contact Us</a></li>
        <li><a href="../contact.html">Request a Quote</a></li>
      </ul></div>
      <div class="footer-col"><h4>Contact</h4><ul>
        <li><a href="mailto:info@softwaresphere.in">info@softwaresphere.in</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <p>© 2025 <span>Softwaresphere</span> (OPC) Private Limited. All rights reserved.</p>
      <p>Built for enterprise-scale transformation.</p>
    </div>
  </div>
</footer>
<script src="../js/main.js"></script>
<script src="../js/faq.js"></script>
</body>
</html>'''

NAV_SCRIPT = '''
const megaToggle = document.querySelector('.mega-toggle');
const megaMenu = document.getElementById('megaMenu');
const accordionButtons = document.querySelectorAll('.mobile-nav .accordion-button');

if (megaToggle && megaMenu) {
  megaToggle.addEventListener('mouseover', () => megaMenu.classList.add('open'));
  megaToggle.addEventListener('focus', () => megaMenu.classList.add('open'));
  document.addEventListener('click', (e) => {
    if (!megaMenu.contains(e.target) && e.target !== megaToggle) {
      megaMenu.classList.remove('open');
    }
  });
}

accordionButtons.forEach((button) => {
  const panel = button.nextElementSibling;
  if (!panel) return;
  button.addEventListener('click', () => {
    const isOpen = button.classList.toggle('active');
    if (isOpen) {
      panel.style.maxHeight = panel.scrollHeight + 'px';
    } else {
      panel.style.maxHeight = null;
    }
  });
});
'''

PAGE_HEADER = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title} – Softwaresphere</title>
<meta name="description" content="{description}"/>
<link rel="stylesheet" href="../css/style.css"/>
<link rel="stylesheet" href="../css/services.css"/>
<link rel="icon" href="../images/logo.png"/>
</head>
<body>
''' + ROOT_NAV + MEGA_MENU + '''
<section class="page-hero">
  <div class="page-hero-label">// {section_label}</div>
  <h1>{hero_title}</h1>
  <p>{hero_desc}</p>
  <div class="breadcrumb"><a href="../index.html">Home</a><span>/</span><span>{breadcrumb}</span></div>
</section>
<div style="max-width:1100px;margin:0 auto;">
'''

PAGE_FOOTER = '''</div>
<section class="section" style="padding:4rem 2rem; text-align:center; background:#FFFFFF; border-top:1px solid var(--border);">
  <div class="section-inner">
    <div class="section-label">// READY TO GET STARTED</div>
    <h2 class="section-title">Ready to Get Started?</h2>
    <p class="section-desc">Talk to our team to scope your service, validate requirements, and begin the engagement.</p>
    <div class="hero-btns" style="justify-content:center; margin-top:1.75rem; gap:1rem; flex-wrap:wrap;">
      <a href="../contact.html" class="btn btn-primary">Talk to an Expert</a>
      <a href="../contact.html" class="btn btn-outline">Request a Custom Quote</a>
    </div>
  </div>
</section>
<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="footer-logo"><img src="../images/logo.png" alt="Softwaresphere"/><div class="footer-logo-text">SOFTWARESPHERE</div></div>
        <p>Enterprise-grade technology solutions across cybersecurity, software engineering, AI, and managed IT infrastructure.</p>
      </div>
      <div class="footer-col"><h4>Services</h4><ul>
        <li><a href="../services/index.html">Services Hub</a></li>
        <li><a href="../contact.html">Contact Us</a></li>
      </ul></div>
      <div class="footer-col"><h4>Company</h4><ul>
        <li><a href="../contact.html">Request a Quote</a></li>
      </ul></div>
      <div class="footer-col"><h4>Contact</h4><ul>
        <li><a href="mailto:info@softwaresphere.in">info@softwaresphere.in</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <p>© 2025 <span>Softwaresphere</span> (OPC) Private Limited. All rights reserved.</p>
      <p>Built for enterprise-scale transformation.</p>
    </div>
  </div>
</footer>
<script src="../js/main.js"></script>
<script src="../js/faq.js"></script>
</body>
</html>'''

WHY_NEED_SECTION = '''<section class="section" style="background:#FFFFFF;">
  <div class="section-inner">
    <div class="section-label">// WHY BUSINESSES NEED IT</div>
    <h2 class="section-title">Why Businesses Need It</h2>
    <div class="section-desc">These services close operational gaps, protect critical assets, and improve decision velocity across the enterprise.</div>
    <div class="features-grid" style="margin-top:2rem;">
      {cards}
    </div>
  </div>
</section>
'''

FEATURES_SECTION = '''<section class="section" style="background:#F8FAFC;">
  <div class="section-inner">
    <div class="section-label">// FEATURES & CAPABILITIES</div>
    <h2 class="section-title">Features & Capabilities</h2>
    <div class="section-desc">The capabilities that help your organization stay secure, modern, and responsive to change.</div>
    <div class="features-grid" style="margin-top:2rem;">
      {cards}
    </div>
  </div>
</section>
'''

INDUSTRIES_SECTION = '''<section class="section">
  <div class="section-inner">
    <div class="section-label">// INDUSTRIES WE SERVE</div>
    <h2 class="section-title">Industries We Serve</h2>
    <div class="section-desc">We support diversified enterprise sectors with tailored technology and security services.</div>
    <div class="services-grid" style="margin-top:2rem;">
      {cards}
    </div>
  </div>
</section>
'''

PROCESS_SECTION = '''<section class="section">
  <div class="section-inner">
    <div class="section-label">// OUR PROCESS</div>
    <h2 class="section-title">Our Process</h2>
    <div class="section-desc">A disciplined delivery process that keeps your initiatives on time and aligned with business goals.</div>
    <div class="features-grid" style="margin-top:2rem;">
      <div class="feature-item"><h4>Discover</h4><p>Understand current state, business needs, and technology constraints.</p></div>
      <div class="feature-item"><h4>Plan</h4><p>Define solution scope, roadmap, and governance for delivery.</p></div>
      <div class="feature-item"><h4>Implement</h4><p>Execute development, configuration, and integration with rigorous oversight.</p></div>
      <div class="feature-item"><h4>Optimize</h4><p>Improve performance, operations, and user experience through iterative refinement.</p></div>
      <div class="feature-item"><h4>Support</h4><p>Provide managed support, monitoring, and continuous improvement after launch.</p></div>
    </div>
  </div>
</section>
'''

FAQ_SECTION = '''<section class="section faq-section">
  <div class="section-inner">
    <div class="section-label">// FREQUENTLY ASKED QUESTIONS</div>
    <h2 class="section-title">Frequently Asked Questions</h2>
    <div class="section-desc">Common questions about how our enterprise services are delivered and supported.</div>
    {faq_items}
  </div>
</section>
'''

FAQ_ITEM_TEMPLATE = '''<div class="faq-item fade-up">
  <button class="accordion-button">{question}</button>
  <div class="accordion-panel"><div class="faq-answer"><p>{answer}</p></div></div>
</div>
'''

def build_cards(features):
    icons = ['⚙️', '📈', '🔒', '☁️', '🧠', '🛠️']
    cards = []
    for index, (title, text) in enumerate(features):
        icon = icons[index % len(icons)]
        cards.append(f'<div class="feature-item"><div class="card-icon">{icon}</div><h4>{title}</h4><p>{text}</p></div>')
    return ''.join(cards)


def build_why_cards(title, description, features):
    generic = [
        ('Reduce operational risk', 'Remove manual gaps, improve visibility, and prevent incidents before they disrupt your business.'),
        ('Strengthen compliance posture', 'Embed the controls and reporting needed for regulation, audits, and board-level confidence.'),
        ('Improve agility', 'Accelerate delivery and response times by standardizing processes and automating repeatable work.'),
        ('Support resilient growth', 'Create a stable foundation that supports new products, channels, and international scale.'),
        ('Preserve continuity', 'Reduce downtime and recovery time by anticipating failure modes and preparing contingency plans.'),
    ]
    return ''.join([f'<div class="feature-item"><h4>{title}</h4><p>{text}</p></div>' for title, text in generic])


def build_industry_cards():
    return ''.join([f'<div class="service-card"><div class="card-icon">🏷️</div><div class="card-title">{industry}</div><p class="card-desc">Solutions designed for {industry} organizations seeking stronger operations and digital resilience.</p></div>' for industry in INDUSTRIES])


def build_faq_items():
    return ''.join([FAQ_ITEM_TEMPLATE.format(question=q, answer=a) for q, a in FAQS[:5]])


def build_page(slug, title, summary, description, features):
    page_title = title
    page_description = f"{summary} - Softwaresphere enterprise services."
    hero_desc = summary
    breadcrumb = title
    page_html = PAGE_HEADER.format(title=page_title, description=page_description, section_label=page_title.upper(), hero_title=title, hero_desc=hero_desc, breadcrumb=breadcrumb)

    paragraph1 = description
    paragraph2 = f"{title} is designed to solve complex enterprise challenges with measurable outcomes and repeatable delivery patterns."
    paragraph3 = "Our team combines technical discipline, security best practices, and pragmatic delivery to make the service dependable in production." 

    page_html += f'''<section class="section" style="background: #FFFFFF;">
  <div class="section-inner">
    <div class="section-label">// WHAT IS {title}</div>
    <h2 class="section-title">What is {title}?</h2>
    <div class="section-desc">{summary}</div>
    <div class="section-text" style="max-width:860px; margin-top:1.75rem; color:var(--muted); line-height:1.8;">
      <p>{paragraph1}</p>
      <p>{paragraph2}</p>
      <p>{paragraph3}</p>
    </div>
  </div>
</section>'''

    page_html += WHY_NEED_SECTION.format(cards=build_why_cards(title, description, features))
    page_html += '''<section class="section" style="background:#F8FAFC;">
  <div class="section-inner">
    <div class="section-label">// WHAT WE PROVIDE</div>
    <h2 class="section-title">What We Provide</h2>
    <div class="section-desc">A clear, checklist-style set of services that support every phase of engagement.</div>
    <div class="features-grid" style="margin-top:2rem;">
      <div class="feature-item"><h4>Assessment</h4><p>Standards-based evaluation of your current controls, processes, and technology.</p></div>
      <div class="feature-item"><h4>Implementation</h4><p>Technical delivery and configuration executed with enterprise governance.</p></div>
      <div class="feature-item"><h4>Monitoring</h4><p>Ongoing visibility, alerts, and operational tracking for continued reliability.</p></div>
      <div class="feature-item"><h4>Optimization</h4><p>Performance tuning, security hardening, and process improvement after deployment.</p></div>
      <div class="feature-item"><h4>Support</h4><p>Dedicated service and expert response to keep your systems stable and compliant.</p></div>
    </div>
  </div>
</section>'''
    page_html += FEATURES_SECTION.format(cards=build_cards(features))
    page_html += PROCESS_SECTION
    page_html += INDUSTRIES_SECTION.format(cards=build_industry_cards())
    page_html += FAQ_SECTION.format(faq_items=build_faq_items())
    page_html += PAGE_FOOTER
    return page_html


def generate_service_pages():
    for slug, title, summary, description, features in SERVICES:
        path = BASE / 'services' / slug / 'index.html'
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(build_page(slug, title, summary, description, features))


def generate_services_index():
    path = BASE / 'services' / 'index.html'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(SERVICES_INDEX_CONTENT)


def generate_nav_script():
    with open(BASE / 'js' / 'mega.js', 'w', encoding='utf-8') as f:
        f.write(NAV_SCRIPT)


if __name__ == '__main__':
    generate_service_pages()
    generate_services_index()
    generate_nav_script()

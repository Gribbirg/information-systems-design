# SportRent System - Project Overview

## Project Description

The **SportRent** system is designed to automate the processes of sports equipment rental, ensure transparent tracking of equipment availability, simplify interaction between clients and administration, and improve resource management efficiency.

## Main Objectives

1. **Automation of Rental Processes** - Streamline the booking, rental, and return procedures for sports equipment
2. **Transparent Inventory Tracking** - Provide real-time visibility of equipment availability and status
3. **Enhanced Client-Administration Interaction** - Simplify communication and transaction processes between users and staff
4. **Efficient Resource Management** - Optimize equipment utilization and operational workflows

## System Scope

The SportRent system encompasses the following key modules:
- **Equipment Catalog Management** - comprehensive inventory and categorization
- **Booking and Orders** - reservation and rental transaction processing
- **Payment Processing** - integrated payment gateway and financial operations
- **Customer Management** - client registration, authentication, and profile management
- **Warehouse Inventory** - equipment tracking, status monitoring, and logistics
- **Database Operations** - data persistence and retrieval services
- **Reporting and Analytics** - business intelligence and performance metrics
- **System Administration** - configuration, security, and user management

## System Architecture

The SportRent system is built on a modern, modular architecture:

- **Architecture Pattern** - Modular structure with 8 independent yet integrated modules
- **API Design** - RESTful API for client-server communication with JSON data exchange
- **Database** - Relational DBMS (PostgreSQL or MySQL) with normalized schema
- **Frontend Technologies** - HTML5, CSS3, modern JavaScript frameworks (React/Vue.js/Angular)
- **Backend Technologies** - Server-side implementation in Python, Node.js, Java, or C#
- **Web Server** - Nginx 1.18+ or Apache 2.4+
- **Communication Protocol** - HTTPS/TLS for secure data transmission

## Key User Roles

- **Clients** - End users who browse equipment catalog, create bookings, process payments, and manage rental history. Can be individuals or organizations seeking temporary access to sports equipment without purchase commitment.

- **Managers** - Business operators responsible for catalog management, pricing strategies, order processing, and business analytics. They ensure smooth business operations, customer satisfaction, and revenue optimization through dynamic pricing and promotional campaigns.

- **Administrators** - System administrators with full access to system configuration, user management, security settings, and technical maintenance. They manage role-based access control (RBAC), audit logs, backup operations, and integration with external systems.

- **Warehouse Staff** - Personnel handling physical equipment operations including issuing equipment to clients, processing returns, conducting condition inspections, maintaining warehouse records, and tracking maintenance schedules.

## Quality Attributes

The system is designed to meet the following quality and performance standards:

### Availability and Reliability
- **System Availability** - 99.5% uptime during business hours
- **Maximum Downtime** - Less than 5 minutes per working day
- **Recovery Time** - System restoration from backup within 4 hours
- **Data Backup** - Automated daily backups with off-site storage

### Performance Metrics
- **Booking Response Time** - Maximum 5 seconds for reservation requests
- **Report Generation** - Maximum 30 seconds for annual data reports
- **Screen Loading** - Maximum 3 seconds for UI form rendering
- **API Performance** - 100 requests per minute with response time under 2 seconds
- **Concurrent Users** - Support for 100+ simultaneous users without performance degradation

### System Reliability
- **Usability Coefficient** - Minimum 90%
- **Data Accuracy** - Minimum 95% information reliability
- **System Restart** - Complete startup/restart within 10 minutes
- **Automatic Recovery** - Self-recovery from temporary failures without data loss

### Security Standards
- **Data Encryption** - HTTPS/TLS for all data transmission
- **Password Security** - Modern hashing algorithms for credential storage
- **Vulnerability Protection** - Defense against SQL injection, XSS, and common attacks
- **Multi-Factor Authentication** - Available for critical operations
- **Audit Logging** - Comprehensive tracking of all data operations
- **Access Control** - Role-based access control (RBAC) implementation

## Project Timeline

The SportRent system development follows a structured 6-month timeline:

**Development Period:** January 15, 2025 - July 15, 2025

### Key Development Stages

1. **Research and Feasibility Study** (Jan 15-25) - Business analysis and market research
2. **Requirements Specification** (Jan 26 - Feb 10) - Technical requirements and system design documentation
3. **Preliminary Design** (Feb 11-25) - Initial architectural decisions and solution proposals
4. **Technical Design** (Feb 26 - Mar 25) - Detailed diagrams, database design, and UI mockups
5. **Development Phase** (Mar 26 - May 25) - Implementation of all 8 system modules
6. **Integration Testing** (May 26 - Jun 5) - Comprehensive system testing in near-production environment
7. **Trial Operation** (Jun 6-25) - Limited user deployment and issue resolution
8. **Production Deployment** (Jun 26 - Jul 15) - Full system rollout and acceptance

## Regulatory Compliance

The SportRent system adheres to Russian and international standards:

### Russian Standards (GOST)
- **GOST 34.602-2020** - Technical specifications for automated systems
- **GOST 34.201-2020** - Documentation types and completeness for automated systems
- **GOST R 59793-2021** - Automated systems development stages
- **GOST R 59795-2021** - Requirements for document content
- **GOST 19.106-78** - Software documentation requirements

### International Standards
- **ISO/IEC 25010:2011** - Systems and software quality requirements and evaluation (SQuaRE)

### Data Protection
- **Federal Law 152-FZ** - Russian personal data protection compliance
- **WCAG 2.1 Level AA** - Web accessibility standards
- **SanPiN 2.2.2.542-96** - Sanitary standards for computer workplaces

## Laboratory Work Structure

Each laboratory work (lab1 through lab8) follows a consistent directory structure:

```
labN/
├── task/
│   └── README.md          # Assignment description and implementation details
└── report/                # Final report and documentation
```

### Directory Descriptions

- **task/** - Contains the assignment requirements, implementation process, source materials, and working documentation for the laboratory work
  - `README.md` - Main documentation file describing the task, approach, and results

- **report/** - Contains the final formatted report ready for submission
  - This directory should include the completed report in the required format (e.g., PDF, DOCX)
  - Follow the guidelines from `/docs/report-formatting-guidelines.md` when preparing reports

# Avalanche Operational Security - Network Simulation

Status: Initial design draft — Version 1

## About This Project

This project models the planned network infrastructure for the company that I would like to start after I graduate from college. Avalanche would provide penetration testing services, hardware installation, and network setup for clients.

The design assumes a roughly 10 person operation with field crews, office support, and cybersecurity specialists. The goal of this project is to demonstrate how the network might operate by creating a browser simulation intended for people with pre-existing knowledge of cybersecurity and network infrastructure. The network is also currently still a work in progress.

## Organization

In my proposed structure for the organization, scheduling and finance fall into their own department, that way I have the ability to focus on reviewing important customer decisions related to the technical aspect.

| Role | People | Responsibilities |
|---|---:|---|
| Owner / Technical Manager | 1 | Supervision over technical and finance departments. Reviewing work and making major customer oriented decisions. |
| Office Operations | 1 | Scheduling, record keeping, coordinating with new clients. |
| Finance | 1 | Payroll, invoicing, expense management and bookkeeping. |
| Field Technicians | 4 | Two crews of two that can handle hardware installs and network setup. |
| Cyber Security Specialists | 3 | Pen testing, report creation and assessment. |
| Total | 10 | |

The field technicians and cyber security specialists would handle separate jobs in the planned 10 person operation. In the beginning, some employees might handle both depending on their experience and workload.

Before an installation, a meeting would be held with the client to discuss the proposal and what the job requires. Each crew would have a company laptop with the files needed for its assigned clients, that way they can access the job information without needing an outside connection. How those files are transferred, protected, updated, and returned after the job is still being decided.

## Systems

The network diagram shows the main devices that the company would use. It does not show a separate computer for all 10 employees, since some devices are there to represent a group of users.

### Firewall / Router

The firewall and router would connect Avalanche's internal network to the internet. It would also control traffic between the network groups where it handles routing. The specific rules and routing setup are still being decided.

### Managed Switch

The managed switch would connect the wired devices, including employee computers, the file server, backup server, printer, and wireless access point. It would support VLANs so devices can be separated into different network groups while using the same physical switch.

### Wireless Access Point

The wireless access point would provide separate staff and guest wireless networks. Employee laptops would connect to the staff network, while visitors would use the guest network. The guest phone in the diagram represents a visitor's device.

### Administrator Computer

The administrator computer would be used to manage the network equipment and company systems. Access to administrative settings would be restricted to authorized users. Who receives those permissions is still being decided.

### Owner's Office Computer

I would have access to all company data areas through a computer in my office. Whether this would be the same computer used for network administration or a separate workstation is still being decided.

### Employee Computers and Crew Laptops

Employee computers would be used for daily work within the company. Each field crew would also have a company laptop with offline access to files for its assigned clients. The applications needed for their work are still being decided.

### Network Printer

The network printer would allow staff to print documents needed for their work. The specific printing permissions are still being decided.

### File Server

The file server currently represents the company's main storage requirement. Files would be separated into areas with their own access permissions. Whether these areas use separate shares, servers, or other storage systems will be decided when the diagram is updated.

### Backup Server

The backup server would collect scheduled backups from the file server and store the newest backup along with the previous four. It would use RAID 6 storage, with protected backups that new backup jobs cannot overwrite. The backup schedule, drive capacity, and method used to lock the backups are still being decided.

## Data Storage and Access

The company would store network diagrams, client proposals, installation instructions and guides, device configurations, penetration testing findings and reports, financial records, and scheduling information.

These files would be separated into storage areas based on who needs access to them. The next revision of the diagram will show how those areas are separated and where the access restrictions are enforced.

### Client Job Files

Each crew would receive only the files needed for its assigned clients. This could include network diagrams, installation instructions, guides, and device configurations needed for the job.

Who approves access to those files is still being decided. Permissions for other employees also need to be worked out.

### Client Proposals

Client proposals would be stored as part of the company's project records. Which employees can view or change them is still being decided. I would have access through my office computer.

### Penetration Testing Findings and Reports

Penetration testing findings and reports would be restricted to the cyber security specialists, with an exception for me as the owner. Office operations would not have access.

Specialists would only access findings while in the office, and reports would also be created there. How assessment data is securely brought back from client sites is still being decided.

### Financial Records

Payroll and financial records would be restricted to finance, with an exception for me as the owner.

### Scheduling Information

Scheduling information would be accessible to finance, office operations, and me as the owner. Whether crews need a limited view of their assigned schedules is still being decided.

### Owner Access

I would have access to all of these storage areas through a computer in my office. Access to business records and permission to change network settings would need to be defined separately.

## Network Separation and Access Rules

I plan to separate the network into staff, guest, server, and management groups. The backup server also needs restrictions on who can connect to it. I still need to decide whether to use a separate backup VLAN, firewall rules on the servers, or both.

The VLAN numbers, subnets, IP addresses, routing, and specific access rules have not been decided yet. File permissions would also depend on what each employee needs for their job. Having different job roles does not mean every department needs its own VLAN.

The file server would not be allowed to start connections to the backup server. It could still respond to connections started by the backup server when collecting a backup. Restoring files would require approval from an administrator.

The office-only restrictions for penetration testing findings and reports would also need to be enforced. The method used to do that is still being decided.

## Backup Design

- The backup server would pull data from the file server on a schedule. The file server would not push backups to it.
- The backup server would use RAID 6 so the storage can keep operating if up to two drives fail. RAID 6 requires at least four drives. The number of drives and storage capacity are still being decided.
- The system would keep five verified backups, including the newest one and the previous four.
- Saved backups would be protected from being changed or deleted while they are locked. A new backup job would not be allowed to write over them. The storage system used to enforce this and how long each backup stays locked are still being decided.
- A new backup would need to be created and checked before the oldest eligible backup is removed. There would need to be room for at least six backups during that process, and possibly more if older backups are still locked.
- An administrator would need to approve restoring files from a backup.

RAID 6 protects against drive failures, but it does not stop someone from changing or deleting files. The pull system and locked backups are separate parts of the design meant to limit that risk. In this project, those features would be simulated rather than used to store real company backups.

The current backup plan covers the file server. If the storage design expands to multiple servers or other systems, the backup scope will need to be updated.

## Simulation Scope and Validation

I want the simulation to show how the network operates during normal use and what happens when access rules allow or block a connection. The individual workflows, failure scenarios, and tests are still being planned.

The simulation would use fictional data. It would show how the rules behave within the project, but I would still need a separate lab to verify actual equipment settings, network isolation, RAID recovery, and backup locking.

## Open Design Questions

- Which jobs could employees handle together when the company is first starting, based on their skills and workload?
- How would files on crew laptops be protected, updated, and returned or removed after a job?
- Would crews need a remote access option if something changes?
- Who would approve access to a client's files, and when would that access be removed?
- Who would be able to view or change client proposals?
- How will the different data areas be separated?
- How will office-only access to penetration testing findings and reports be enforced?
- How would assessment data be securely returned from client sites?
- Would my office computer be separate from the administrator computer?
- Would crews need a limited view of their assigned schedules?
- Would penetration testing tools and practice systems have their own separate lab network?
- How often would backups run, how long would they stay protected, and how much lost work or downtime could the company accept?
- What VLANs, subnets, services, and access rules would the network use?

## Project Ownership and AI Assistance

I came up with the business concept, drew the original network layout, and made the final decisions about the requirements and planned behavior of the network. Those decisions include how crews access client files, which employees can access sensitive records, and how backups should be collected and protected.

I used ChatGPT as a brainstorming and review tool to ask questions, suggest options, and help me work through technical concepts. It also helped organize and revise the documentation and refine my original diagram through AI image editing.

This project is still in the design stage. Implementation and testing have not been completed yet.
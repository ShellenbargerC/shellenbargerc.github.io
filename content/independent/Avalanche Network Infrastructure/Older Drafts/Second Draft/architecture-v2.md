# Avalanche Operational Security - Network Simulation

Status: Second design draft - Version 2

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

Office operations would manage scheduling and assign crews to jobs. I would approve access to the client files needed for each assignment.

## Systems

The network diagram shows the main devices that the company would use. It does not show a separate computer for all 10 employees, since some devices are there to represent a group of users.

The second physical layout includes five separate physical servers, separate owner and administrator computers, representative department workstations, and the smart laptop locker.

The diagram uses colored dots to identify roles and system functions. These colors do not represent completed VLAN configuration or mean that devices with the same color have unrestricted access to each other.

### Firewall / Router

The firewall and router would connect Avalanche's internal network to the internet. It would also control traffic between the network groups where it handles routing. The specific rules and routing setup are still being decided.

### Managed Switch

The managed switch would connect the wired devices, including the five physical servers, office workstations, administrator computer, printer, wireless access point, and smart laptop locker.

It would support VLANs so devices can be separated into different network groups while using the same physical switch. Each wired device shown in the diagram would have its own connection to the switch.

### Wireless Access Point

The wireless access point would provide separate staff and guest wireless networks. Employee laptops would connect to the staff network, while visitors would use the guest network. The guest phone in the diagram represents a visitor's device.

### Administrator Computer

The administrator computer would be used to manage the network equipment and company systems. Access to administrative settings would be restricted to authorized users. Who receives those permissions is still being decided.

This computer would be physically separate from my office computer.

### Owner's Office Computer

I would have access to all company data areas through a computer in my office.

This would be a separate workstation from the administrator computer used to manage network equipment and servers. Access to company data and permission to change system settings would be defined separately.

### Employee Computers and Crew Laptops

Employee computers would be used for daily work within the company. The diagram includes representative workstations for office operations, finance, and cyber security specialists.

Each field crew would also have a company laptop with offline access to approved files for its assigned clients.

Crew laptops would be collected in the morning and returned at the end of the day. The applications needed for their work and the method used to protect local files are still being decided.

### Smart Laptop Locker

A smart laptop locker would be installed at the main office for crew laptop checkout and return. It would connect to the managed switch, with its network group and allowed connections still being decided.

The locker would release the assigned laptop after employee authentication, job authorization, file approval, and device readiness checks pass. It would record who collected the laptop and when it was returned.

The locker would handle physical release and return. Preparing job files, reviewing returned data, and removing old client files would be separate processes.

### Check-In and Assignment System

Employees would use a check-in screen at the main office to receive their prepared daily assignment. The screen could be built into the locker or provided through a separate device.

The check-in system would communicate with the job assignment and laptop checkout services hosted on the Operations Server.

Office operations would be available to answer questions about assignments.

### Network Printer

The network printer would allow staff to print documents needed for their work. The specific printing permissions are still being decided.

## Physical Server Layout

The design would use five separate physical servers. Each server would connect to the managed switch.

Separate physical machines would not replace the need for permissions, network restrictions, updates, or recovery planning.

### Business File Server

The Business File Server would store client proposals, network diagrams, installation instructions and guides, and device configurations.

Files would still be separated into areas with their own permissions. Crews would only receive approved files needed for their assigned clients.

### Security Server

The Security Server would store penetration testing findings and reports.

Access would be restricted to the cyber security specialists while in the office, with an exception for me as the owner using my office computer. Reports would also be created in the office.

### Finance Server

The Finance Server would store payroll and financial records.

Access to those records would be restricted to finance, with an exception for me as the owner.

### Operations Server

The Operations Server would host scheduling, job assignment, and laptop checkout services.

The system would provide different views based on the employee's role. Office operations would manage the full schedule, employees would see their own scheduled work times, and finance would see the work times needed for payroll without job details or destinations.

The checkout services would support the smart locker by checking assignments, approvals, and laptop readiness. The exact software, authentication integration, and service permissions are still being decided.

### Backup Server

The Backup Server would be a separate physical machine with RAID 6 storage.

It would initiate scheduled backups from the Business File Server, Security Server, Finance Server, and Operations Server.

Each working server would have its own independent backup history containing the newest verified recovery point and the previous four. New backup jobs would not be allowed to overwrite protected recovery points.

Backup schedules, drive capacity, retention periods, and the method used to lock backups are still being decided.

## Diagram Color Categories

The colors identify roles and system functions. Actual access permissions would be enforced separately.

| Color | Category | Devices shown |
|---|---|---|
| Blue | Staff | Business File Server, crew laptop, network printer |
| Red | Security | Security Server, security workstation |
| Gold | Finance | Finance Server, finance workstation |
| Cyan | Operations | Operations Server, office operations workstation, smart laptop locker |
| Green | Backup | Backup Server |
| Purple | Administration | Administrator computer |
| Pink | Owner | Owner's office computer |
| Orange | Guest | Guest phone |

The internet connection, firewall/router, managed switch, and wireless access point remain neutral because they support multiple roles and network groups.

Solid lines represent wired connections. Dotted lines represent wireless connections.

## Scheduling and Daily Assignments

The proposed scheduling system would separate employee work times from detailed job assignments.

- Each employee would see their own scheduled work times.
- Office operations would manage the full schedule, crew assignments, job locations, and related job information.
- Finance would see the work times needed for payroll without seeing client job details or where crews are going.
- I would have access to the full schedule and job information as the owner.

Employees would report to the main office in the morning to check in and receive their assignment before leaving as a two person crew.

The assignment would include the job location, contact information, instructions, and approved files needed for that day's work.

How changes during the day are communicated and how actual hours are recorded are still being decided. Scheduled work times and actual hours worked would need to be tracked separately.

## Client Job Preparation

Before an installation, a meeting would be held with the client to discuss the proposal and what the job requires.

Office operations would assign a crew to the job. I would approve the client files that the crew needs access to.

The approved files would be prepared on the crew laptop before release. Those files would be available offline, that way the crew would not need an outside connection to access its job information.

How the files are securely transferred, who prepares the laptop, and how changes to the job package are handled are still being decided.

## Laptop Checkout and Return

### Morning Checkout

Each two person crew would collect its prepared company laptop from the smart locker in the morning.

Before release, the system would check:

- The employee's company badge.
- The employee's fingerprint.
- The employee's assignment to the job.
- Approval for the client files loaded on the laptop.
- Whether the assigned laptop is ready for use.

Checkout would be recorded against the named employee collecting the shared crew laptop.

### Authentication and Recovery

Employees would need both their company badge and a successful fingerprint check for normal laptop release.

If either authentication check fails, the locker would remain locked. The proposed recovery process would require me to separately verify the employee's identity before approving a one-time release for that employee, laptop, and job.

This approval would not bypass approved file permissions or laptop readiness checks. Failed authentication attempts and recovery approvals would be logged.

Fingerprint enrollment, protection of biometric records, and the method used to verify identity during recovery are still being decided.

What happens if I am unavailable to approve recovery is also still being decided.

### End-of-Day Return

The employee would return the laptop to the locker and sign it back in when the crew returns at the end of the day.

A returned laptop would not automatically become available for another job. It would remain unavailable until returned files and device readiness checks have been handled.

Who reviews the returned files, updates the master records, removes old client files, and prepares the laptop for its next assignment is still being decided.

### Planned Laptop States

- Prepared: The approved job files have been loaded.
- Ready: Required checks have passed and the laptop can be released.
- Checked out: The laptop has been released to a named employee.
- Returned: The laptop has been checked back into the locker.
- Awaiting checks: Returned files and device condition still need to be processed before the laptop becomes ready again.

The detailed checks and transitions between these states still need to be defined.

## Data Storage and Access

The company would store network diagrams, client proposals, installation instructions and guides, device configurations, penetration testing findings and reports, financial records, and scheduling information.

These would be distributed across the Business File, Security, Finance, and Operations Servers. Files and services on each server would still need their own access permissions.

The physical diagram shows where the systems connect. A logical network diagram would show the network boundaries and where access restrictions are enforced.

### Client Job Files

Each crew would receive only the files needed for its assigned clients. This could include network diagrams, installation instructions, guides, and device configurations needed for the job.

These files would come from the Business File Server.

I would approve access to those files. Permissions for other employees and when crew access is removed still need to be worked out.

### Client Proposals

Client proposals would be stored on the Business File Server as part of the company's project records.

Which employees can view or change them is still being decided. I would have access through my office computer.

### Penetration Testing Findings and Reports

Penetration testing findings and reports would be stored on the Security Server and restricted to the cyber security specialists, with an exception for me as the owner. Office operations would not have access.

Specialists would only access findings while in the office, and reports would also be created there.

How assessment data is collected and securely brought back from client sites needs to be worked out so that the field assessment process fits with the office-only restrictions.

### Financial Records

Payroll and financial records would be stored on the Finance Server.

Access would be restricted to finance, with an exception for me as the owner.

### Scheduling Information

Scheduling and assignment information would be managed through the Operations Server.

Finance would have access to work times needed for payroll without access to client job details or worker destinations.

Office operations would have the full job schedule. Employees would see their own scheduled work times and receive detailed assignments when checking in at the main office.

### Owner Access

I would have access to all of these data areas through the separate computer in my office.

Access to business records and permission to change network settings would be defined separately.

## Network Separation and Access Rules

The initial design identified staff, guest, server, and management groups. The revised design now has separate physical systems for business files, security reports, finance, operations, and backups.

The final network groups and VLAN boundaries still need to be designed. The diagram's color categories do not automatically mean each category will have its own VLAN.

The backup server and laptop locker also need restrictions on who and what can connect to them.

I still need to decide whether backup isolation uses a separate backup VLAN, firewall rules on the servers, or both.

The VLAN numbers, subnets, IP addresses, routing, and specific access rules have not been decided yet. File permissions would also depend on what each employee needs for their job. Having different job roles does not mean every department needs its own VLAN.

None of the four working servers would be allowed to start connections to backup storage. They could still respond to connections initiated by the Backup Server when collecting backups.

Restores would require approval from an administrator. The backup system would send the selected data to the original server or a replacement. Working servers would not have unrestricted access to pull files from backup storage.

The office-only restrictions for penetration testing findings and reports would also need to be enforced. The method used to do that is still being decided.

The smart locker would need controlled access to the authentication, assignment, and checkout services it uses. Those connections will be defined when the logical network layout is developed.

## Backup Design

- The Backup Server would pull data from the Business File, Security, Finance, and Operations Servers on a schedule.
- The four working servers would not push backups or initiate connections to backup storage.
- The Backup Server would use RAID 6 so the storage can keep operating if up to two drives fail. RAID 6 requires at least four drives. The number of drives and storage capacity are still being decided.
- Each working server would have its own independent history of five verified recovery points, including its newest backup and the previous four.
- Across the four working servers, the normal retained history would total 20 recovery points. This does not mean the backups would all be the same size.
- Saved recovery points would be protected from being changed or deleted while they are locked. A new backup job would not be allowed to write over them.
- The storage system used to enforce locking and how long each recovery point stays locked are still being decided.
- A new recovery point would need to be created and checked before that server's oldest eligible recovery point is removed.
- There would need to be room for a sixth recovery point for each server being backed up during rotation, and possibly more if older recovery points are still locked.
- A failed backup job would not cause an existing verified recovery point to be removed.
- An administrator would need to approve restoring files from a backup.
- The backup system would send approved restore data to the original server or a replacement.

RAID 6 protects against drive failures, but it does not stop someone from changing or deleting files. The pull system and locked backups are separate parts of the design meant to limit that risk.

The backup scope now covers all four working servers. Any additional systems introduced later would need their backup requirements reviewed.

In this project, these features would be simulated rather than used to store real company backups.

## Simulation Scope and Validation

I want the simulation to show how the network operates during normal use and what happens when access rules allow or block a connection.

The planned scope now also includes employee check-in, assignment release, laptop checkout, and laptop return. The individual workflows, failure scenarios, and tests are still being planned.

The simulation would use fictional company and client data. Badge IDs and fingerprint results would also be simulated. The project would not collect actual fingerprints or other biometric data.

The simulation would show how the rules behave within the project, but I would still need a separate lab to verify actual equipment settings, network isolation, RAID recovery, backup locking, and locker integrations.

## Changes Since the First Draft

- Added more detailed storage categories and access requirements.
- Assigned scheduling and crew job assignments to office operations.
- Assigned approval of crew client-file access to me as the owner.
- Proposed separate schedule views for employees, finance, and office operations.
- Added morning check-in and daily assignment collection.
- Added a smart laptop locker for morning checkout and end-of-day return.
- Added badge and fingerprint authentication for laptop release.
- Proposed owner-approved recovery when authentication fails.
- Added laptop readiness and return-processing requirements.
- Chose separate physical servers for business files, security reports, finance, operations, and backups.
- Assigned scheduling, job assignment, and laptop checkout services to the Operations Server.
- Expanded backup collection to all four working servers.
- Chose five independent recovery points for each working server.
- Confirmed that my office computer would be separate from the administrator computer.
- Updated the physical diagram with the five servers, department workstations, and smart locker.
- Removed the diagram's grouping boxes and added colored role and function categories.
- Left VLANs, routing, technical access controls, and remaining operational details open for further development.

## Open Design Questions

- Which jobs could employees handle together when the company is first starting, based on their skills and workload?
- Who prepares the approved files and loads them onto crew laptops?
- How would files on crew laptops be protected, updated, and returned or removed after a job?
- Would crews need a remote access option if something changes?
- When would crew access to a client's files be removed?
- Who reviews returned files and prepares laptops for the next job?
- How would actual hours worked be recorded?
- How would schedule or assignment changes be communicated during the day?
- Who would be able to view or change client proposals?
- What permissions are needed within each server's files and services?
- How will the separate physical servers be placed into network groups?
- How will office-only access to penetration testing findings and reports be enforced?
- How would assessment data be securely returned from client sites?
- Who would receive administrative access to network equipment and servers?
- How would employee badges and fingerprints be enrolled and managed?
- How would identity be verified if normal locker authentication fails?
- What happens if I am unavailable to approve authentication recovery?
- What happens if the locker or one of its supporting systems is unavailable?
- What software and integrations would run on the Operations Server?
- Would penetration testing tools and practice systems have their own separate lab network?
- How often would backups run, how long would they stay protected, and how much lost work or downtime could the company accept?
- What hardware specifications and storage capacities would each server need?
- What VLANs, subnets, services, and access rules would the network use?

## Project Ownership and AI Assistance

I developed Avalanche's business concept, drew the original network layout, and made the design decisions documented in this project. For Draft 2, I expanded the design to include separate physical servers, role-based access requirements, independent backup histories, and controlled laptop checkout.

I used ChatGPT to discuss and review the design, clarify questions, and help organize and revise the documentation. The updated diagram was generated with AI image editing based on my original drawing and the changes I directed.

This is a design project in progress. Implementation and testing will be documented as development continues.
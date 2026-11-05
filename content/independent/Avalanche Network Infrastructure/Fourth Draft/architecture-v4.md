# Avalanche Operational Security - Network Simulation

Status: Draft 4 - Planned infrastructure, not yet implemented or tested

## About This Project

This project models the planned network infrastructure for the company that I would like to start after I graduate from college. Avalanche would provide penetration testing services, hardware installation, and network setup for clients.

The design assumes a roughly 10 person operation with field crews, office support, and cybersecurity specialists. The goal of this project is to demonstrate how the network might operate by creating a browser simulation intended for people with pre-existing knowledge of cybersecurity and network infrastructure. The network is also currently still a work in progress.

## New in Draft 4 - Packet Tracer Build Planning

Status: Draft 4 planning checkpoint complete - Implementation and testing pending

The previous design content is retained below. This section records the decisions for Draft 4.

### Office Personnel and Computer Counts

The planned company would still have 10 employees: one owner, one office operations employee, one finance employee, four field technicians, and three cyber security specialists.

The first Packet Tracer build would show a separate workstation for each of the three cyber security specialists. The office computer count would be:

| Computer | Quantity | Planned use |
|---|---:|---|
| Owner's Office Computer | 1 | Review company records and technical decisions |
| Office Operations Workstation | 1 | Scheduling, assignments, and client coordination |
| Finance Workstation | 1 | Payroll and financial work |
| Security Workstations | 3 | Office access to findings and report creation |
| Administrator Computer | 1 | Authorized system and network administration |
| Total wired computers | 7 | |

The administrator computer would be a separate device, not an additional employee. Each specialist's workstation would remain subject to the existing security data access requirements.

### Crew Laptops and Spare Equipment

The first build would include three crew laptops. Each of the two field crews would have one laptop, and the third would be a spare if an assigned laptop breaks.

The spare would not represent another crew or employee. Before release for a job, it would still need the appropriate approved files, assignment, checkout, and readiness checks. The process for switching an assignment to the spare is still being decided.

### Automatic and Fixed Network Addresses

Everyday office workstations, crew laptops, and guest devices would receive their network addresses automatically through DHCP. This would include the Office Operations workstation, Finance workstation, and three Security workstations.

The owner's office computer and administrator computer would use static addresses. The servers, network equipment management interfaces, network printer, and smart laptop locker would also use static addresses.

This would provide automatic setup for everyday devices and predictable addresses for infrastructure and the two designated computers. Address assignment would not replace authentication or access permissions.

### DHCP Service Location

The firewall/router would provide DHCP for everyday office workstations, crew laptops, and guest devices in the first Packet Tracer build. A separate DHCP server would not be added for this build.

Each network using DHCP would receive settings appropriate to its own VLAN. The existing static addressing decision for infrastructure, the owner's office computer, and the administrator computer would remain.

### Infrastructure Server

A separate physical Infrastructure Server would provide internal DNS, time synchronization, and centralized logging. This would bring the planned physical server count to six, including the Backup Server.

DNS would allow company services to be reached by name. Time synchronization would help keep device timestamps consistent. Centralized logs would collect supported device activity for troubleshooting and review.

The Infrastructure Server would use its own VLAN and a static address, following the decision to separate physical server roles into their own networks. DHCP would remain on the firewall/router.

This would not yet assign employee authentication or locker authentication to the Infrastructure Server. Those services, access to collected logs, backup coverage for the new server, and service recovery arrangements are still being decided.

### Infrastructure Server Backup Coverage

The Backup Server would also collect protected backups from the Infrastructure Server. Its backup history would contain five independent verified recovery points, following the same requirements as the other source servers.

The backup scope would now cover five source servers: Business File, Security, Finance, Operations, and Infrastructure. The normal retained history would total 25 recovery points across those servers.

Infrastructure backups would include the service configuration and retained logs needed for recovery. The exact backup contents, schedules, retention periods, and recovery tests are still being decided.

### Office-Only Printing

The network printer would be available to office computers only. Crew laptops and guest devices would not be allowed to print through the company network.

Printing access would not grant permission to change printer settings. Printer administration and any controls for collecting sensitive printed documents are still being decided.

### Consistent Internal Addressing

The first build would use a consistent internal addressing pattern. Each selected VLAN number would match the third part of its IP subnet, using the pattern 10.10.<VLAN number>.0/24. The router gateway for each of these networks would use the .1 address.

This would make the network groups easier to identify in configuration notes and troubleshooting. The specific VLAN numbers and device addresses would be recorded in the network architecture document.

### Separate Printer Network

The network printer would use its own VLAN, separate from office computers, crew laptops, guest devices, servers, and the smart laptop locker. Office printing connections would pass through the firewall/router so that access rules can control the permitted connections.

Printing would remain available to office computers only. Crew laptop and guest printing would remain blocked. Printer administration would require separate permissions.

### Shared Security Workstation Network

The three cyber security specialist workstations would share one Security workstation VLAN. The Security Server would remain in its own separate server VLAN.

This would group computers with the same planned role while keeping their server connections subject to the firewall/router's access rules. Each specialist would still need the appropriate identity and access permissions.

### Dedicated Computer for Remote Administration

The administrator computer would be the only computer allowed to remotely access management interfaces on company servers and network equipment in the first build. Authorized administrative credentials would still be required.

My office computer would retain approved access to company data, but would not be used for remote system administration. Everyday workstations, crew laptops, and guest devices would not receive remote management access.

Physical console access would remain a separate recovery method. Who receives administrative accounts, how those accounts are protected, and the physical recovery procedure are still being decided.

### Separate Crew and Guest Wireless Access Points

The first Packet Tracer build would use two wireless access points. One would provide staff Wi-Fi for crew laptops, and the other would provide guest Wi-Fi. This would replace the single representative access point in the earlier physical layout.

Each access point would connect to the managed switch in its assigned VLAN. Crew laptop access would follow the approved internal service rules. Guest Wi-Fi would remain password protected, with internet access allowed and internal company access blocked.

Wireless equipment models, wireless names, crew wireless authentication, and the exact configuration are still being decided.

### Administrator Computer Location and Access

The administrator computer would remain a separate physical computer from the owner's office computer and everyday office workstations. It would be placed in the server room. This would relocate the existing administrator computer, not add another computer or employee.

Access would require a badge, biometric verification, and a sign-in log. Whether badge and biometric checks apply to server room entry, computer sign-in, or both is still being clarified. The exact logging process and authorized users are still being decided.

The existing requirement for authorized administrative credentials would remain. Physical access would not automatically grant permission to administer systems.

### Badge and Biometric Checks at Both Access Points

Badge and biometric verification would be required both when entering the server room and when signing into the administrator computer. Passing the door checks would not automatically sign the employee into the computer.

Server room entry and administrator computer sign-in would each have a separate sign-in record. Authorized administrative credentials would still be required for system changes.

This resolves the earlier question about where the checks would apply. Enrollment, authorized users, recovery when a check fails, and protection of the authentication records are still being decided.

### Crew Laptop Internet Restrictions at the Office

Crew laptops would not have internet access while connected to Avalanche's office network. They would only be allowed the approved internal connections needed for their work and supporting network services.

Approved transfers between the internal Business File Server and crew laptops would remain part of the planned workflow. The laptops would still use approved job files offline at client sites.

Software updates would need a separately planned controlled process. This decision does not define connections to client networks or internet access away from the office.

### End of Draft 4 Checkpoint

Draft 4 closes with the current equipment counts and the agreed addressing, supporting service, backup, printing, wireless, and administrative access decisions. The design would include seven wired computers, three crew laptops, six physical servers, and separate crew and guest wireless access points.

The administrator computer would remain separate from the owner's computer and be placed in the server room. Badge and biometric checks would apply at both the room door and administrator computer sign-in, with separate sign-in records.

The authorized technical employee would remain responsible for preparing approved job files and reviewing returned files. Whether this employee signs into each crew laptop for direct transfers to and from the Business File Server has not been decided.

The next draft would complete the remaining build choices and begin the Packet Tracer topology in stages. Software update handling, offsite laptop access, authentication integrations, and other open operational questions would remain visible as the design develops. No implementation or testing is claimed in this draft.

## Previous Design Content

The following content is retained from the previous drafts. Where an older section leaves a question open or gives an earlier equipment count, the confirmed Draft 4 updates above take precedence. Unresolved questions remain open.

## Previously Established Network Design Decisions

### Central Routing and Traffic Control

For the first Packet Tracer build, the firewall/router would handle traffic between the VLANs. The managed switch would connect the devices and place their connections into the assigned VLANs.

This would provide a central place to control communication between network groups. Employee access to company files and application features would still need separate permissions.

The VLAN boundaries and specific access rules are still being decided. This is a planned arrangement and has not been implemented or tested yet.

### Finance Workstation and Server Separation

The Finance workstation and Finance Server would be placed in separate VLANs. Their communication would pass through the firewall/router so that access rules can control the permitted connections.

Finance would still need the appropriate application and file permissions. The exact services and permitted connections are still being decided.

### Security Workstation and Server Separation

The Security workstation and Security Server would be placed in separate VLANs. Their communication would pass through the firewall/router so that access rules can control the permitted connections.

Access to findings and reports would remain restricted to cyber security specialists while in the office, with an exception for me as the owner using my office computer. VLAN separation would be one part of the access controls. The exact services, permissions, and controls for office-only access are still being decided.

### Business File and Operations Server Separation

The Business File Server and Operations Server would be placed in VLANs separate from employee computers. Employee connections to these servers would pass through the firewall/router so that access rules can control the permitted connections.

Whether these two servers share a server VLAN or use separate VLANs is still being decided. Employee access to client files, schedules, assignments, and checkout services would still need the appropriate file and application permissions.

### Separate Network Groups for All Five Servers

Each of the five physical servers would have its own VLAN and IP subnet: Business File, Security, Finance, Operations, and Backup. The server VLANs would also be separate from employee computers.

Traffic between these server networks would pass through the firewall/router, where access rules would control the permitted connections. Separate VLANs would not automatically authorize servers to communicate with each other.

This decision resolves the earlier question about whether the Business File Server and Operations Server would share a server VLAN. They would use separate VLANs. The existing backup collection and restore requirements would remain.

### Guest Internet Access

Guest Wi-Fi would provide internet access only. Guest devices would not be allowed to access internal company networks, including company servers, employee devices, the printer, the smart laptop locker, or equipment management interfaces.

Guests would still receive the basic network services needed for internet connectivity. The technical arrangement for those services is still being decided.

### Guest Wireless Authentication

Guest Wi-Fi would be password protected. The password would be provided to guests visiting the office rather than offering an open wireless network. Guest access would remain limited to the internet, with internal company access blocked.

Wireless coverage could extend beyond the building. Knowing the password would not establish that a device is physically inside the office. Password rotation and any individual or temporary guest credentials are still being decided.

### Crew Laptop Network Separation

Crew laptops would use their own VLAN while connected to the company network, separate from office workstations and server networks. Their company connections would pass through the firewall/router so that access rules can limit them to the services needed for their work.

The existing requirements for approved offline job files, laptop checkout, return processing, and readiness checks would remain. The exact permitted network connections are still being decided.

### Crew Laptop File Transfers

The job-file transfers discussed for crew laptops would be between the laptops and the internal Business File Server. Internet access would not be required for these internal transfers.

Only the approved files needed for the assigned job would be prepared for offline use. Returned files would still need to be reviewed before master records are updated. Who performs these steps and how the transfers are handled are still being decided.

Internet access for software updates or other crew laptop uses has not been decided.

### Technical Responsibility for Crew Job Files

An authorized technical employee would prepare the approved job files for crew laptops and review returned files. I would still approve which client files each crew is allowed to receive as the owner.

Preparing the files would follow that approval. Reviewing returned files would remain separate from the locker's physical return function, and returned files would not automatically update master records.

The employee's specific permissions, the process for updating master records, and responsibility for the remaining laptop readiness checks are still being decided.

### Smart Laptop Locker Network Separation

The smart laptop locker would use its own VLAN, separate from employee computers and server networks. Its connections to the Operations Server and authentication services would pass through the firewall/router so that access rules can control the permitted connections.

This would not replace the existing badge, fingerprint, assignment, file approval, and laptop readiness checks. The location of the authentication service and the exact permitted connections are still being decided.

### Previous Design Checkpoint

The next draft would define the remaining network groups, VLAN IDs, subnets, supporting services, permitted connections, and Packet Tracer build and test plan. The design remains planned infrastructure and has not been implemented or tested yet.

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
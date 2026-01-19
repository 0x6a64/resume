---
title: "CWWK X86-P2 J4105 Mini PC/Router"
description: "CWWK X86-P2 Crashing on Power Saving Enablement"
pubDate: "Jan 18, 2026"
heroImage: "_images/router.jpg"
tags: ["OPNsense", "Networking"]
---

When I was setting up my CWWK X86-P2 a couple years ago, I ran into an unusual problem that I'm documenting here in case it helps anyone else. Similar issues may exist on more recent versions of these boxes. I had the CWWK box mostly configured with OPNsense, and everything was working flawlessly. However, I wanted to enable power saving to minimize power consumption, especially during evening hours when the router would see minimal traffic.

Every time I enabled PowerD, the system would become highly unstable. This instability persisted regardless of which power profile I selected or which tunables I adjusted. Unfortunately, since I was configuring the device for the first time, I had changed many settings at once and wasn't entirely sure what was causing the issue. After some testing and reviewing the logs, I realized it was related to PowerD. Further research on the OPNsense forums revealed that similar models were experiencing this issue. The consensus was that this type of system instability can occur when processor microcode packages are not installed. OPNsense's BSD base doesn't include the appropriate microcode packages on install. Sure enough, after SSHing into the OPNsense machine and installing the cpu-microcode-intel package, the problems disappeared and the system was able to use PowerD and various power profiles without crashing.

Since I installed that fix, OPNsense has released a plugin that can be installed via the GUI called os-cpu-microcode-intel. I hope this helps someone troubleshoot similar system instability issues in the future.

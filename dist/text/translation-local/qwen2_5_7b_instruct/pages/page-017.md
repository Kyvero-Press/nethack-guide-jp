# Page 017

Choose "Copy". After the copy is finished, go back to the 98 Note Menu and select "Mode Settings", then set "System Boot Device I" to "Standard", "System Boot Device II" to "FD", and "First Drive Designation" to "FD" again. After setting, set the "Boot Disk" to the floppy drive and press the (ESC) key twice to exit the 98 Note Menu. This time, the floppy drive should boot as drive A.

From this state,

B: INSTFD B A

should be entered and the (④) key pressed.

Then, various messages will appear on the screen, which basically means that the NetHack program is being expanded onto the "Boot Disk". If instructed to change disks halfway through, please insert the "Data Disk" into the floppy drive. The CG data and other data will be expanded onto the "Data Disk".

If EMS is available, it would be good to copy the EMS driver you usually use to the "Boot Disk" and set it up in CONFIG.SYS. However, the specifics of how to do this would vary, so we will not go into detail here.

■ Installation to Hard Disk

If you want to install NetHack to a hard disk, at least 3MB of free space is required. First, start MS-DOS, set the attached disk to the floppy disk drive, and move to that drive. Specifically, if the drive where the floppy disk was inserted is B:

B: INSTALL

This is the state from which you should proceed.

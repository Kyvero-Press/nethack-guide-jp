# NetHack Guide — local English translation (Qwen2.5-7B-Instruct)

Source OCR: Surya. Generated locally with vLLM. This is a machine translation for human evaluation.


## Page 001

3.5"2HD
5'2HD

For PC-9801
Free Software Library

Game Collection HK Special

NetHack

For PC-9801

Free Software Library
Game Collection Extra
NetHack

The RPG

Edited by
Tatsuhiko Rokkai

Published by Showa System Trading Co., Ltd. Price: 2,800 yen (net 2,718 yen)

ISBN 4-87966-322-0 C3055 P2800E


## Page 002

■ Note

• Reproduction of any part or all of the contents of this book without written permission from the publisher is prohibited regardless of policy.

• The author and publisher cannot be held responsible for the results and effects of using the contents of this book and the attached disk.

• The software included in the appendix disk is generally free software that can be used and distributed, with each author holding the copyright. For details, refer to the documentation of each software.


## Page 003

PC-9801 Version

Free Software Library

Game Collection Extra

NetHack

an
RPG

Edited by

Tatsuhiko Rinko

SHUWA
SYSTEM
TRADING
CO.,LTD.


## Page 004

Preface

Welcome to the world of NH!

Do you know the game called "NetHack—ネットハック"? It is one of the free software programs. To be honest, it is not a particularly well-known game.

Still, if you enjoy playing games on your computer, you have probably heard of "ROUGE—ローグ" at least once or twice. NetHack is an advanced version of this ROUGE game.


## Page 005

NetHack the RPG—with FMP & MAG loader—

Table of Contents

DISK Usage of Attached Disk 10

• Requirements Necessary Items 10

• Install Installation 11

• Start Up! Method of Startup 16

• More Info. For Reference 18

CHARACTERS Characters 23

• Parameter Ability Values 23

• Class Occupation 26

• Be Invoked NetHack Activation 39

COMMANDS Commands 43


## Page 006

When ASCII began offering "Rogue" as one of its services during the trial period, many lines were filled with "Rogue" players, and there were even users who spent over ten thousand yen. As a result, the service was stopped due to this.

What could be so interesting about it? Unlike the abundance of RPGs in the world, the characters in "Rogue" or "NetHack" lack flavor and personality. There are no cute female characters, and it is far from having animations or conversations with PCM.

In ordinary RPGs, players are often represented as two-headed characters. However, in this world, players are simply represented by "@". The various monsters and dungeon contents are also shown using characters that can be displayed on a computer—such as "o" and "r".

The game itself is quite illogical. No matter how well you progress, you might end up with a game over for a small reason. It might be a game that makes you want to give up if you are accustomed to balanced RPGs.

However, I still find myself playing "again…", even though it is a game with a strange charm. Someday, you too may see yourself in "@", and "o" as a goblin.

Once you are drawn into the charm of this game, you will likely play "NetHack" all day on a sunny holiday… just like the authors! 

Good luck, and happy hacking!


## Page 007

ITEMS Items 144

• Amulets Amulet 144

• Armors Armor 145

• Foods Food 158

• Potions Potion 161

• Rings Ring 165

• Scrolls Scroll 169

• Spellbook Spellbook 173

• Tools Tool 178

• Wands Wand 185

• Weapons Weapon 188

MONSTERS Monsters 205

• A~Z 206

• a~z 225

• その他記号 Othersymbols 245

INFORMATIONS To conquer the dungeon 250

COMMAND LIST

265


## Page 008

NetHack General Public License

(Copyright 1989 M. Stephenson)

(Based on the BISON general public license,
copyright 1988 Richard M. Stallman)

Everyone is permitted to copy and distribute verbatim copies of this license, but changing it is not allowed. You can also use this wording to make the terms for other programs.

The license agreements of most software companies keep you at the mercy of those companies. By contrast, our general public license is intended to give everyone the right to share NetHack. To make sure that you get the rights we want you to have, we need to make restrictions that forbid anyone to deny you these rights or to ask you to surrender the rights. Hence this license agreement.

Specifically, we want to make sure that you have the right to give away copies of NetHack, that you receive source code or else can get it if you want it, that you can change NetHack or use pieces of it in new free programs, and that you know you can do these things.

To make sure that everyone has such rights, we have to forbid you to deprive anyone else of these rights. For example, if you distribute copies of NetHack, you must give the recipients all the rights that you have. You must make sure that they, too, receive or can get the source code. And you must tell them their rights.

Also, for our own protection, we must make certain that everyone finds out that there is no warranty for NetHack. If NetHack is modified by someone else and passed on, we want its recipients to know that what they have is not what we distributed.

Therefore we (Mike Stephenson and other holders of NetHack copyrights) make the following terms which say what you must do to be allowed to distribute or change NetHack.


## Page 009

COPYING POLICIES

1. You may copy and distribute verbatim copies of NetHack source code as you receive it, in any medium, provided that you keep intact the notices on all files that refer to copyrights, to this License Agreement, and to the absence of any warranty; and give any other recipients of the NetHack program a copy of this License Agreement along with the program.

2. You may modify your copy or copies of NetHack or any portion of it, and copy and distribute such modifications under the terms of Paragraph 1 above (including distributing this License Agreement), provided that you also do the following:

a) cause the modified files to carry prominent notices stating that you changed the files and the date of any change; and

b) cause the whole of any work that you distribute or publish, that in whole or in part contains or is a derivative of NetHack or any part thereof, to be licensed at no charge to all third parties on terms identical to those contained in this License Agreement (except that you may choose to grant more extensive warranty protection to some or all third parties, at your option)

c) You may charge a distribution fee for the physical act of transferring a copy, and you may at your option offer warranty protection in exchange for a fee.

3. You may copy and distribute NetHack (or a portion or derivative of it, under Paragraph 2) in object code or executable form under the terms of Paragraphs 1 and 2 above provided that you also do one of the following:

a) accompany it with the complete machine-readable source code, which must be distributed under the terms of Paragraphs 1 and 2 above; or,

b) accompany it with full information as to how to obtain the complete machine-readable source code from an appropriate archive site. (This alternative is allowed only for noncommercial distribution.)

For these purposes, complete source code means either the full source


## Page 010

Distribution of NetHack as originally released over Usenet or updated copies of the files in this distribution used to create the object code or executable.

4. You may not copy, sublicense, distribute, or transfer NetHack except as expressly provided under this License Agreement. Any attempt otherwise to copy, sublicense, distribute, or transfer NetHack is void and your rights to use the program under this License agreement shall be automatically terminated. However, parties who have received computer software programs from you with this License Agreement will not have their licenses terminated so long as such parties remain in full compliance.

Stated plainly: You are prohibited by the terms of this License Agreement from using NetHack for gainful purposes. You are permitted to modify NetHack, or otherwise use parts of NetHack, provided that you comply with the conditions specified above; in particular, your modified NetHack or program containing parts of NetHack must remain freely available as provided in this License Agreement. In other words, go ahead and share NetHack, but don't try to stop anyone else from sharing it farther.


## Page 011

NetHack General Public License (Translation)

(Copyright 1989, 1990 M. Stephenson)

(Based on the Bison General Public License:

Copyright 1988 Richard M Stallman)

Anyone can copy and distribute this license, but it cannot be modified. The expressions used in this license can be used to create conditions for other programs.

Most software company license agreements are decided unilaterally by those companies. In contrast, our general public license aims to give everyone the right to share NetHack. To ensure that you can indeed have these rights, we must prohibit anyone from denying your rights or demanding their abandonment.

In particular, we want to ensure that you can give copies of NetHack to others, obtain the source code, change NetHack or use part of it in a new free software, and know that you can do these things. We want to make sure that you have these rights.

To ensure that everyone can indeed have these rights, we must prevent you from taking these rights away from others. For example, if you distribute a copy of NetHack, you must give all of your rights to the recipient. You must ensure that they can obtain the source code as well. And you must teach them their rights.

Additionally, to protect ourselves, we must make it clear to everyone that there are no warranties regarding NetHack. We want those who obtain a modified version of NetHack to be able to recognize that it was not distributed by us.

Therefore, we (Mike Stephenson and other NetHack copyright holders) set the following conditions for you to obtain permission to distribute or modify NetHack.

The rest is omitted, refer to the English version.


## Page 012

Appendix Disk Usage Instructions

Disk

Due to various modifications made to the NetHack included on the attached disk, it is theoretically possible to play it using a floppy disk, but practically impossible. A hard disk or EMS would be ideal. Let's start by explaining how to prepare to play NetHack.

Requirements Necessary Items

There are several things you need to prepare to play the NetHack included on the attached disk.

First, let's list the absolutely necessary items.

Firstly, a PC-9801 VF or later model with at least 640 KB of main memory is absolutely required. In other words, any series of PC-9801 with a CPU version V30 or higher, and PC-286/386/486 series would work. Machines released within the last 2 to 3 years should suffice.

And, MS-DOS version 3.1 or later is also necessary.

Next, let's list some desirable items to have. First, a hard disk. Since the attached disk includes NetHack background music (BGM) and image CGs, using them would require two floppy disks.

Additionally, if you have expandable memory that can be used as EMS and the corresponding EMS driver, that would be great. While NetHack can run without it, performance will be significantly slower, making it practically unplayable.

Also, it would be nice to have an English-Japanese dictionary, and plenty of

10

DISK—Appendix Disk Usage Instructions


## Page 013

Time. These two might be necessities to complete NetHack.

Install - インストール

■Floppy Disk Installation

As I have mentioned repeatedly, playing NetHack on a computer with only floppy disks is very difficult. However, it's not impossible, so let me explain the procedure for installing onto a floppy disk.

First, please prepare two double-sided high-density (2 HD) floppy disks.

Insert the MS-DOS system disk into drive A and an empty disk into drive B, then boot the computer. Once the MS-DOS system has booted...

From the state of...

Enter `FORMAT B: /M /S` and press the key.

Then, the disk drive will start formatting the disk in drive B. When this process is finished, remove the disk from drive B. We will call this disk the "boot disk," so it would be good to put a label on it saying so. Now, insert the other disk into drive B...

From the state of...

Enter `FORMAT B: /M`


## Page 014

Enter the command and press the Enter key. Then, the disk drive will move again to format the B drive disk. When the processing is finished, it is good to remove the B drive disk and stick a label saying "Data Disk" on it.

Next, take out the MS-DOS system disk from the A drive and set the "Boot Disk" as a replacement, then reset the computer to restart it.

And after MS-DOS has started, set the attached disk to the B drive. Thereafter, ...

From the state of ...

Type B: INSTFD B A and press the Enter key.

12 DISK—Usage of Attached Disk


## Page 015

Then, various messages will appear on the screen, essentially indicating that the NetHack program is being expanded onto the "boot disk". If instructed to change disks halfway through, please put the "data disk" into drive A. The CG and other data will be expanded onto the data disk.

Afterwards, if EMS is available, it would be good to copy the EMS driver you usually use onto the boot disk and set it up in CONFIG.SYS. Although the specifics of how to do this would get into individual instructions, we will omit them here.

■ Installation on a Notebook Computer (RAM Drive)

On a notebook computer, you can play NetHack somewhat comfortably if you make good use of the RAM drive (if there is an internal hard disk, installing to it would be better). The basic installation method is the same as with floppy disks, but there are still several things to keep in mind.

First, before starting the installation, you need to save the contents of the RAM drive. If the contents of the RAM drive can be lost without issue, you can start by booting while pressing the HELP key to display the 98 Notebook menu, then selecting "RAM Drive → Floppy Disk Copy" to move the RAM drive's contents onto one floppy disk.

Next, set the MS-DOS system disk in the floppy drive and choose "Auto Mode" to boot. After booting, set a new floppy disk in the floppy drive and...

From this state,

FORMAT B: /M /S

should be entered and the key pressed.

Install——Installation

13


## Page 016

Then the floppy disk will be formatted. So, after processing is finished, remove the disk and put a label on it saying "Boot Disk". Now, put another floppy disk into the floppy drive ...

...from this state,

TYPE FORMAT B: /M

and press the ④ key. Then, as the disk will be formatted again, remove the disk after processing is finished and put a label on it saying "Data Disk".

Next, copy the contents of the attached disk to the RAM drive. Put the floppy disk containing the attached disk in the floppy drive, and reset while pressing the (HELP) key. Then, in the 98 Note Menu, select "Floppy Disk → RAM Drive"


## Page 017

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


## Page 018

B:

Type B and press the key. Then...

B>

if it becomes this state, type...

INSTHD B A

and press the key. By the way, A refers to the installation target hard disk. It might be that A and B are assigned as hard disks and C and D as floppy disks, depending on the user. In such cases, please input appropriate drive names instead.

After that, follow the instructions displayed on the screen until the installation is complete.

Start Up! Starting Method

If installed on a floppy disk, set the "Boot Disk" to A drive and the "Data Disk" to B drive, then reset the computer to boot it up. After a while, the disk will start working, and the menu screen will be displayed along with the message "Welcome to NetHack." Note that if you do not set SW 3-4 to OFF (LCD reverse display) under "System Setup" → "Dip Switch Setup," the character CG may be unviewable. Regardless, be prepared that the screen may be difficult to see on monochrome LCD displays. Here, input your player's name, your cat's name, your favorite fruit, etc., move the cursor using the cursor keys to choose your profession, and press the key to start the game.

After the game ends, to restart, use the following command:

NTHK

16

DISK—Usage of Attached Disk


## Page 019

Note that if you have installed the RAM drive version on a notebook computer, set the floppy drive with the "boot disk" and start the computer while pressing the (HELP) key. Choose "Auto Mode" from the 98 Notebook menu. When the menu screen appears with the message "Welcome to NetHack," reinsert the data disk into the floppy drive, enter your name and other information, choose your class, and press (J) to start the game.

If you want to restart after quitting once, use the following commands to boot up.

NTHK (J)

If you have installed it on a hard disk, first start the computer and then move to the installation destination. If you installed NetHack on the B drive, ...

Starting from ...

B: (J)

... type this (this is unnecessary if it was installed on the A drive). Then,

CD games & nethack (J)

... and type to move to the directory.

NTHKPATH (J)

... and finally,

NTHK (J)

Start Up! — How to Start

17


## Page 020

When you input ..., the message "Welcome to NetHack" will appear along with the menu screen. Enter the player's and pet's names, choose a profession, and press N to start the game.

To restart, use the following command again.

NTHK N

Note that when starting NetHack, at least 450 KB of free memory area is required. Especially if using it on a hard disk, it is recommended to check using programs like CHKDSK.EXE or VMAP.COM. When using CHKDSK.EXE, the free memory area is indicated at the end of the display. If this number is 450000 or more, you can play NetHack. Ideally, however, you would want around 520 KB of free memory area. If it is insufficient, please remove the Japanese FEP or take other measures. The specific operation method varies depending on the reader's environment settings, so I will omit the explanation.

More Info. For reference

The following explanation is merely for reference, so you can skip it without any problem. However, it might be useful information for those who understand.

■ NETHACK.CNF

NETHACK.CNF is a file that records the usage environment for NetHack. Since the attached disk includes an additional program for the NetHack startup menu, there is no need to modify NETHACK.CNF. However, if you set up NETHACK.CNF appropriately, you can start NetHack directly without going through the startup menu.

18

DISK——Usage of the Attached Disk


## Page 021

For example, my NETHACK.CNF is as follows:

OPTIONS=!pickup,number_pad,time
OPTIONS=98_BIOS,rawio,98graphics
OPTIONS=name:Avelna-R,female,
                dogname:Suezow,catname:Patty,fruit:satuma
HACKDIR=A:\GAMES\NETHACK
LEVELS=A:\GAMES\NETHACK\BONES
SAVE=A:\GAMES\NETHACK\BONES;n

In this case, the character's name is Avelna, the class is Rouge, and it is female. The dog's name is Suezow, the cat's name is Patty, and the favorite fruit is satuma (orange). Additionally, it shows that PC-9800 series-specific features are utilized, and NetHack is installed in the directory "A:\GAMES\NETHACK".

Normally, if you want to modify it, you would change the three lines related to character and pet settings. The "-R" after the name indicates the class, and classes correspond to English letters as follows:

AArcheologistBBarbarianCCavemanEElf

HHealerKKnightPPriestRRogue

SSamuraiTTouristVValkyrieWWizard

Regarding fruits, melons, oranges, bananas, apples, and pears already exist in the game, so you need to specify other types of fruits.

Also, for notebook computers or other models without a numeric keypad, you can remove the "98_BIOS" on the second line and the "number_pad" on the first line. This allows you to move the character or specify directions using b,j,n,h,l,y,k,u instead of the numeric keypad. Not doing this would require pressing (NUM) lock each time.

Lastly, note that the last three lines specify directories. These should be the actual drive and directory where NetHack is installed.


## Page 022

If you have misread the configuration and set it incorrectly, NetHack will not start.

NetHack. Even if you properly set up CNF, to start NetHack, you need to move to the directory first...

Simply enter...

NetHack

...and the game should start immediately.

■ Startup Options

If you want to directly start the game and let a friend play, or change your name occasionally to try a different mood, you can input...

NetHack -uYositune

The characters after -u become the character's name. Similarly, if you want to try a different class occasionally...

NetHack -English

Enter this. The part after -English should be the initial letter of the class name in uppercase.

■ Starting in Immortality Mode

The game NetHack is very difficult. Beginners will quickly erect dozens of tombstones. Therefore, there is an immortality mode (discovery-mode). To start playing in immortality mode...

NetHack -X

...will work. When your hit points reach 0 and you die, you will be asked if you died. By entering n, you can revive yourself.

Note that changing your name, selecting your class, and specifying immortality mode can all be done at the same time.

20

DISK——Usage of Attached Disk
SOURCE


## Page 023

You can do so. If you want to play as a priest named Tike in invulnerable mode...

NETHACK -uTike -P -X

...you can start it this way.

■ FMP and MAG

In the attached disk of this book, in addition to the original NetHack, CGs are included, and we have used SAM's free software called "MAG Loader" to realize the display of background CGs. Since MAG Loader is a separate program from NetHack, you can view the CGs individually, but for that, you need to enter from the MS-DOS prompt ...

MAG file name (□)

...and input (make sure that MAG.EXE can be executed at the path where the file is located and pay attention to the file path).

The file names of each CG are as follows:

ArchelogistNTHK_A PriestNTHK_P

BarbarianNTHK_B RougeNTHK_R

Cave-manNTHK_C SamuraiNTHK_S

ElfNTHK_E TouristNTHK_T

HealerNTHK_H VarklieNTHK_V

KnightNTHK_K WizardNTHK_W

The BGM is also specially created for the attached disk of this book, and we have used guu's free software called "FMP" to perform it. Of course, an FM sound source board is required for the performance. You will need an FM sound source board built-in or installed externally.

With the CG display and the title back and BGM during play, three songs are prepared respectively. To listen to these songs individually, you need to follow the following procedure.

More Info.—Reference—

21


## Page 024

First, have FMP resident. From the MS-DOS command line, enter as follows:

When FMP's theme music plays, this means that you are ready to listen to the background music (BGM). To play a song here, do the following:

The file names of each song are as follows:

Chaotic character title background

Neutral character title background

Lawful character title background

BGM 1

BGM 2

BGM 3 (for Speak & Spell)

BGM 3 is fully compatible only with a somewhat special FM sound source board called Speak & Spell, so it will be incomplete on regular FM sound source boards. It may be a bit difficult to listen to, but please bear with us.

Note that there are also programs where songs can be specified via the menu. These are...

and by entering the above, you can start them. After starting, you can specify the file name using cursor movement and key ①.

22

DISK—Usage of Attached Disk


## Page 025

In the world of NetHack, various parameters and professions are set for the characters you send into this world. Therefore, each character has its own personality due to these settings.

Parameter Ability Values

Let's show information regarding the parameters needed to discern a character's abilities. These are mainly displayed on the two lines below the status line on the NetHack screen.

St: Strength

Strength  Strength

The higher this parameter is, the more robust and powerful the character will be in terms of physical strength. It determines the damage dealt with weapons and how much weight the character can carry in Yendor's dungeon.

For warrior-type characters, this parameter must be excellent above all else. Additionally, magic users also need a certain level of strength to cast spells.

Dx: Dexterity

Dexterity Agility, Finesse

In combat, a high Dexterity is necessary for hit rates and performing tasks that require nimbleness such as picking locks or disarming traps.

Thief-type characters must have nimble hands. The fate of an inept thief … is a tragic one.

Parameter——Ability Values

23


## Page 026

Co : Constitution

Constitution Vitality

The higher your Constitution, the more advantageous you are in withstanding vitality drain and escaping damage from poison. It also has a significant relationship with the increase in hit points when leveling up.

As a warrior, it is desirable to have a high Constitution. A warrior who excels in strength but is physically weak would be nothing but a laughing matter.

In : Intelligence

Intelligence Intellect

Intelligence affects the ability to cast spells. When reading magic books to learn spells, a value of Intelligence is required. How can an illiterate person read a magic book?

Of course, those who practice magic will need a great deal of Intelligence.

Wi : Wisdom

Wisdom Wisdom

It is often related to dealings with gods. Gods prefer wiser beings. In order to store the energy required for magic, one must be much wiser than ordinary humans.

Priests (or Priestesses) who serve as agents of the gods likely receive their favor due to their wisdom.

Ch : Charisma

Charisma Charm

The presence or absence of Charisma directly affects negotiations with shopkeepers who run stores in Yendor's dungeon. The prices they charge for their goods are almost nonexistent, and the more charming the buyer, the more willing they are to sell items at a lower price.

By the way, Charisma encompasses not just physical appearance but also the overall charm of a person (or other monsters, which may also be possible). While there is no zero in terms of physical appearance.

24

CHARACTERS—Your Doppelganger Sent to the Dungeon


## Page 027

The above six parameters are usually represented within the range of 3 to 18. However, strength can exceed 18 in some cases, and when it does, it is written as "18/xx". Additionally, there are instances where a certain item can raise strength to over 25.

Now, let's consider a rogue with a strength of 14, dexterity of 18, constitution of 13, intelligence of 10, wisdom of 8, and charisma of 7. Let's think about this rogue's personality based on these six parameters.

Firstly, he is somewhat strong and has decent endurance. His nimbleness and speed are unparalleled. However, regarding his intellect, he can barely read. His judgment may not be entirely accurate, but he never acts in a completely unconventional manner. He comes across as somewhat gruff and tends to irritate those around him... This character sketch should give you a sense of what a seasoned NetHack player is like.

Furthermore, in NetHack, there are attributes. These are similar to the GOOD/NEUTRAL/EVIL types in Wizardry, and they consist of LAWFUL/NEUTRAL/CHAOTIC.

LAWFUL means a character who is obedient to social order, while CHAOTIC refers to a character who disregards social order and follows their own path (of course, if their thoughts align with societal ideals, they will follow that path. They are not simply mischievous). NEUTRAL signifies a character who falls between these two extremes. Of course, these attributes do not remain constant throughout one's life; they can change based on the character's actions.

Attributes:
LAWFUL
NEUTRAL
CHAOTIC
Social Adaption Type
Middle Type
Anti-Social, Free Spirit Type

Parameters—Ability Values

25


## Page 028

However, there are things that speak more eloquently of a character's nature than these parameters and attributes. Those are classes (occupations).

NetHack offers 12 different occupations. Some may boast strength, while others may excel in magic. Some might be captivated by ancient treasures. It would be wonderful to color your character in such a way. They are never mere game pieces but rather characters born into the world of NetHack.

### Class 职业

The occupations available in NetHack number twelve. Each has its strengths and weaknesses, and it's hard to say which is best. However, no matter the class, you can eventually clear the game, so I hope you play patiently.

Of course, some classes are better suited for beginners, while others are not. The author recommends Barbarian or Valkyrie for beginners. Both classes meet the necessary condition of having many hit points, which is crucial for surviving in NetHack. Additionally, both dislike spells, which means they won't rely on troublesome magic.

On the other hand, Archaeologist and Tourist are not recommended for beginners. While the former might be an interesting character for veteran players, it could be a bit tough for beginners who are not yet accustomed to the NetHack world. Tourists are not necessarily for advanced players. In fact, they might be the most enjoyable class just for playing, but they are too challenging for beginners.

Once you have become somewhat familiar with NetHack, I also recommend playing Rogue, Priest, or Sorcerer. By the way, the author's current favorite class is Rogue.

26

CHARACTERS—Your Doppelganger Sent to the Dungeon


## Page 029

Archeologist

Archeologist: Archaeologist

This archeologist is dressed somewhat like a scholar and somewhat like an adventurer. An archeologist who skillfully wields a long whip and wears a leather hat would be recognizable as being based on someone (the person from a famous movie! ).

They, the archeologists, venture into the dungeons of Yendor to discover the ancient treasures rumored to be hidden there. Of course, they can move through the dungeon stealthily, finding treasures—though even if they trigger a trap and giant stones start rolling towards them, they can still escape (whether such traps exist in Yendor's dungeons is another matter).

Archeologists, due to their profession, have deep knowledge of gems. They can identify any gem at a glance—although this does not apply to those enchanted by magic.

Moreover, they excel in survival skills and possess a special item that allows them to manufacture canned goods from monster materials (a rare treasure rarely found in the dungeons of Yendor). Thanks to this tool, archeologists who stockpile food are immune to starvation. However, this tool is very heavy, so it would be foolhardy for those with low strength to carry it.

Attributes: Cowardly Direct Combat: △ Magic: △ God: Quetzalcotl

Class——Profession

27


## Page 030

Barbarian

Barbarian: Barbarian

A barbarian can be described as the archetypal warrior we imagine. Wearing sturdy armor that provides safety commensurate with its weight, he smashes everything with his longsword.

They often prefer to fight more directly than they think. Generally, their muscle reactions are much faster than their brain's thinking. They boast an abnormally strong physique, but are practically ignorant when it comes to magic. If they find a spellbook in Yendor's dungeon, it would be foolhardy to touch it. There is nothing to lose by not reading it, and it could fetch some gold coins if sold at a shop.

The barbarians seek honor, something they cannot obtain through any other means, and venture into Yendor's dungeon. Their great physical strength is surely sufficient to break through the traps and monsters lurking in the dungeon.

Moreover, due to their excessive physical strength, no poison can penetrate their bodies.

Attributes: Chaotic

Direct combat: √

Magic: ×

God: Morrigan

28

CHARACTERS—The doppelgangers you send into the dungeon


## Page 031

Caveman / Cave-Woman

Caveman: Caveman
Cavewoman: Cavewoman

They come from afar, seeking something—perhaps a value system unknown to us—and challenge the dungeons of Yendor. These are the Cavemen (or Cavewomen).

Their ability to run across plains and climb wild mountains clearly makes them suited for warriors. However, their equipment is somewhat lacking. The cudgels they used on the plains can be considered too weak as weapons in the dungeons of Yendor. Additionally, their armor consists of the skins of animals they hunted, which, when viewed as armor, is quite poor. Therefore, it is necessary for Cavemen to search for new weapons and armor immediately upon entering the dungeon.

They carry a bow in one hand, which they use to hunt prey. They are excellent warriors and hunters, on par with or even surpassing elves in skill.

Moreover, it may seem unbelievable, but the god they worship belongs to the side that brings order. Although they may appear barbaric at first glance, this is simply because Cavemen are rough.

Attributes: Lawful

Direct combat: √

Magic: ×

God: Anu

Class——Vocation

29


## Page 032

Elf

Elf: Elf

They are called elves in human legends, but in reality, they are closer to subhumans. There are several races, and there are various differences in their characteristics depending on the race. Their bodies are generally one size smaller than humans, and they are not particularly robust. And because of their pointed ears and almond-shaped characteristic eyes, those who do not know of elves would see them as small, strange humans.

So, this eye can be said to be the most notable ability of the elves. The eyes of the elves are specially made. Human eyes can see transparent objects that are invisible to them.

Furthermore, elves are generally skilled archers. Moreover, this powerful vision allows them to easily spot hidden doors, passages, and traps. The value of these elf-specific abilities in Yendor's dungeon can be understood only by actually going to Yendor's dungeon.

Elves head towards Yendor's dungeon out of their rare curiosity. They often wear beautiful short swords, finely crafted by elves, and light yet sturdy chainmail for exploration. Of course, it is unthinkable for them, born hunters, to forget their bows and arrows.

Attributes: Cowardly

Direct combat: △

Magic: △

God: Solonor Thelandira

30

CHARACTERS——The doppelgangers you send to the dungeon


## Page 033

Healer

Healer: Healer

A healer can be considered quite a unique existence as an adventurer. In terms of personality, they are close to priests, possessing numerous healing potions and books of healing spells. However, their healing power does not rely on divine intervention but rather on their own means such as medicine and magic. They venture into the depths of the dungeon of Yendor in search of spirit herbs.

However, when it comes to combat, they can be considered complete novices, just like priests. When they enter the dungeon, the only weapon they carry is a small knife. And the only piece of armor they wear is a glove to prevent their skin from being affected by drugs.

However, all healers possess a special stethoscope that allows them to instantly discern the abilities of monsters. This will provide them with much wisdom in the dungeon of Yendor. It is said that if used correctly, this stethoscope can guide them to use various medicines to turn battles against monsters into advantageous ones.

And due to handling too many chemicals, it is said that they have resistance to all poisons.

Attributes: Cowardly

Combat Direct: ×

Magic: √

God: Athena

Class——Occupation

31


## Page 034

Knight

Knight: Knight

A knight is a proud warrior clad in various armor. Their steeds cannot enter Yendor's dungeon, but their noble and compassionate spirit can even move merchants who run shops in the dungeon to offer them a few discounts.

While not as much as clerics, knights also possess enough wisdom to receive divine favor. In fact, one could say that a knight is a warrior-cleric. Although they cannot distinguish blessings from curses, only knights and clerics can use their god's power to annihilate creatures that have been born in the realm of death.

Furthermore, knights wear many pieces of armor such as mail, gauntlets, and helms, so their defensive power upon entering the dungeon ranks among the highest of the 12 professions.

Unfortunately, the strength and dexterity of knights, which are crucial for combat, are not particularly noteworthy. One might say they are somewhat lacking in these areas.

In case of emergency, it is best to pray to the gods for help.

Attributes: Lawful Direct Combat: √ Magic: × God: Lugh

32

CHARACTERS—Your Doppelganger Sent to the Dungeon


## Page 035

Priest / Priestess

Priest: Priest

Priests challenge the dungeons of Yendor as a trial to elevate their own faith. Their nature makes them particularly receptive to prayers addressed to the gods compared to any other humans or elves. Additionally, they possess considerable skill in magic—especially in healing. The only class allowed to carry two spellbooks when entering the dungeon is the priest.

As a result of their training, priests have the ability to discern blessings and curses. This ability is highly effective in surviving the dungeons of Yendor. There is nothing more pitiful than seeing an adventurer covered in cursed weapons and armor. Priests will not wear cursed items. This is the greatest favor granted by the gods to priests. Furthermore, like knights, priests can use divine power to annihilate cursed creatures that possess the origin of life in the realm of death.

However, they do not possess notable combat abilities. Yet, their kicks are powerful enough to break treasure chests and sometimes kill monsters with a single blow. Could this also be a divine favor?

Attributes: Neutral

Melee Combat: △

Magic: ○

God: Crom

Class——Occupation

33


## Page 036

Rogue

Rogue: Thief

Originally, "Rogue" means something like "rascal." However, due to their profession, they are often called "thieves." They carry tools for picking locks and can easily open treasure chests or coffins. Of course, keys to doors are nothing to them. They go to the dungeons of Yendor, rumored to hide great treasures, to hone their thieving skills and to obtain these treasures.

Moreover, as a result of training, they possess the skill to walk without making any noise. Even if there is a sleeping monster in a room of the Yendor dungeon, it is easy for them to pass by the monster without waking it up.

The main weapon of a thief is a short sword that is easy to maneuver, and they prefer leather armor because they dislike noisy metal armor. Additionally, they are skilled in handling poison. It is often said that the darts they throw are coated with poison.

Attributes: Chaotic

Melee combat: △

Magic: △

God: Rat God

34

CHARACTERS—The doppelgangers you send to the dungeon


## Page 037

Samurai

Samurai: Samurai

They serve only their lord——the word "samurai" means one who stands by his lord——and believe that the soul of their sword has been transferred to it… The lonely warriors of a small island nation in the far east are samurai. They are knights of the far east, proud and noble. They carry two katana, the name given to their large and small swords, and shuriken, star-shaped throwing knives.

Why do they challenge the dungeons of Yendor? The truth of this is known to no one other than the samurai themselves. Samurai hold firm resolve within their hearts and head toward the dungeons to fulfill that resolve.

It goes without saying that they carry several fortune cookies as a favorite food. Additionally, like monks, samurai possess powerful kicking strength. Against shallow-level monsters, they can easily defeat them with their kicks rather than using their katana.

Attributes: Lawful

Melee combat: ○

Magic: △

God: Amaterasu Omikami

Class——Class

35


## Page 038

Tourist

Tourist: Traveler

The tourist is just a regular person. They have no notable abilities. Why did they come to this terrifying dungeon? There is no room for debate. They came to the famous Yendorian dungeon as tourists!

Their main weapon is darts, but their camera could be considered their true weapon. The flash of this expensive camera can blind monsters living underground who are not accustomed to bright light.

Moreover, the Hawaiian shirts they wear—their only armor—are something shopkeepers should beware of, as they might try to disguise themselves as camouflaged creatures. Additionally, they carry credit cards, but cash is the only form of payment accepted in Yendor's dungeon. However, there is no need to worry about the tourist's funds. They possess a large amount of cash. Perhaps they plan to buy souvenirs in the dungeon.

They also carry a magic mapping scroll—a scroll that reveals the dungeon's layout. If by any chance they were to conquer the dungeon, it would be a great shame for Yendor.

Attributes: Neutral

Combat: None

God: Chih Sung-tzu

36

CHARACTERS—Your avatar sent to the dungeon


## Page 039

Valkyrie

Valkyrie: Female Warrior

The Valkyrie is a maiden who wields a shield—a female warrior. Originally, they referred to twelve goddesses who served the supreme god Odin in the north. However, over time, they have come to mean female warriors in general. They may also be called Valkyries depending on the location.

They boast combat power equal to or greater than that of Barbarians. Unlike the ruggedness of Barbarians, they wield monsters with supple muscles. And like Barbarians, they are also not easily felled by the claws and fangs of monsters.

Moreover, Valkyries are famous for bringing very few items into the Dungeons of Yendor. First, they carry one longsword and one shortsword as weapons. They also carry a small shield that boasts excellent defensive capabilities through magic. And there is only one piece of food. They do not even wear armor.

For some reason, they can endure cold without wearing any clothes. Whether it is due to magic or nature, this has no bearing on them.

Attributes: Chaotic

Melee Combat: √

Magic: ×

God: Loki

Class——Occupation

37


## Page 040

Wizard

Wizard: Magic User

As the name suggests, they are a person skilled in magic arts. They are practically unskilled in close combat, and their preferred weapons are limited to small swords. Moreover, while they have enough stamina to cast basic spells, their physique, which has been shaped by a life of continuous magical research, seems far removed from the term "robust."

When venturing into the dungeon, these magic users carry several magical items. These include one spellbook, one magic wand, and two magic rings.

If they cannot skillfully use these items, it will be impossible for them to survive the dungeon of Yendor with such a frail physique.

However, their diverse array of magical skills more than makes up for their weakness in close combat. Provided you can acquire many spellbooks… That being said. If you find a spellbook in the dungeon shop, you should sell everything you own to buy it. For them to survive, they must learn as much magic as possible. 

Attributes: Neutral

Melee Combat: ×

Magic: √

God: Thoth

38

CHARACTERS—Your Doppelganger Sent into the Dungeon


## Page 041

Be Invoked NetHack Start

Now, when you start the game, you will notice that several parameters other than attributes such as Strength are displayed on the two lines at the bottom of the screen. These represent the character's status.

On the far left of the first line is the character's name. Next to the name, something like "XXXX the Plunderer" is written, which is the title. This title changes along with the character's level. After the title, the aforementioned parameters are listed. These parameters are also not constant and change due to various factors during gameplay. On the right end of the first line, the character's attributes are written.

The second line shows the current status of the character. The leftmost part, DIvI, indicates which floor of the dungeon the character is on. To its right, G: represents the gold the character is carrying.

Next to the gold, the hit points are written. These points decrease due to enemy attacks, and if they reach zero, the character dies and the game ends.

You hear the footsteps of a guard on patrol.

| . . . . . < || . . . . . #-----

| . . . . . |#% . . . | ###- . . . { . |

| . . . . . |# ! . . . | ## . . . . . |

| . . . . . +# ! $ . . . #####| . . . . . ------

| . . . . . |# . ) . . . | #- . ---- . -# . % . |

| . . . . . |####-----####! . . . . |

----- . -----# #########+ . . . . |####

# ##### ###

###### # ## ## -----## ####

###### #- . . . | - -############## ### - . -

--- . -----+### ## ! . |

| . . . . . { . |### -----#> @ . . |# # . $ . |

| . . . . . |### | . . . | #| . . . . . |####| . . . . .

| . . . . . |# ### | { . . . | #| . . . . . |#####| . . . . .

| . . . . . .### #+ . % . | #| . . . . . |##| . . . . .

-----| . . . . #| . . . | #| . . . . .

Yoshitune the Bushi St:18/03 Dx:10 Co:18 In:10 Wi:10 Ch:8 Lawful
DIv1:3 G:101 HP:11(49) Pw:25(25) AC:4 Xp:5/247 T:434
C1 CU CA S1 SU VOID NWL INS REP *Z

Be Invoked——NetHack Start

39


## Page 042

When it overflows, the number in parentheses represents the maximum hit points. No matter how much rest or potion you consume, recovery will not exceed this value.

To its right, Pw: stands for mana. It decreases every time a spell is cast. As expected, if this number is below the mana required for a spell, even if you have memorized the spell, you cannot use it.

AC: means armor class. This armor class indicates the strength of the armor equipped by the character. The lower the number, the better. A negative number is even better.

To its side, Xp is experience points. The left number is the level, and the right number is the experience points. When the experience points exceed a certain value, the level increases. As the level rises, hit points increase, and resistance to poison and magic improves. T: indicates the elapsed time.

Additionally, next to the elapsed time, the state of fullness is shown. If in normal condition, nothing is displayed. When fully satiated, it shows Satiated; when hungry, Hungry; when too weak due to extreme hunger, Weak; and when fainted due to starvation, Fainting. Fainting makes it impossible to walk, and eventually, death by starvation occurs. Ensuring food supply can be considered the top priority.

Next to the state of fullness, the condition of the body is often shown. When confused, it shows Conf; when sick, Sick; when blind, Blind; when stunned, Stun; and when under the effect of certain drugs or after eating a specific monster, it shows Hallu.

At the very top of the screen, the surroundings and the outcome of battles with monsters are depicted as messages. For example, sounds heard or special events occurring around the character (such as a pet suddenly disappearing from sight) are described in English. Also, the names of items on the ground, thrones, springs, and other objects present there are displayed.

Or, the options for the character's actions may also be shown in this line. For example, when discarding an item, options like "What do you want to drop? [$ad-fi-kw or? *]" are displayed to choose which item to discard. 

40

CHARACTERS——Your Doppelganger Sent to the Dungeon


## Page 043

And in the central part of the screen, what the character has found in the dungeon is displayed. Below, I will explain what the following characters mean:

a~z: Various monsters nesting in the dungeon

A~Z: Open doors on the vertical or horizontal walls of the room

;&: Open doors on the horizontal or vertical walls of the room

||: Floor of the room, or entrance without a door

——: Passage, or sink in the kitchen, or movable bridge

..: Stairs up

##: Stairs down

<>: Closed door, or spellbook

++: Human (player), or a monster in human form

@@: Gold coin

$$: Trap (not displayed until discovered or triggered)

^^: Weapon (weapon)

)): Armor

[[: Food (includes monster corpses)

%%: Scroll with spells or various effects

??: Wand

//: Ring

==: Potion of water

!!: Various tools

((: Amulet or spider's web

””: Jewel or pebble

**: Rock or statue

00: Iron ball (used as leg irons for some sin)

——: Altar, or iron chain to attach the iron ball to the convict

}}: Puddle or moat (falling into it causes drowning)

{{: Fountain

¥¥: Luxurious throne (something may happen if you sit on it)

Be Invoked——NetHack Start

41


## Page 044

Now, these symbols construct Yendor's dungeon, and to walk around within it, you must move your character using the numeric keypad. However, if you are using a notebook computer or other device without a numeric keypad, you can use the cursor keys or lock the (NUM) key and use it instead.

@ represents the character

Note that if there is a monster in the direction you wish to move, you will attack with your weapon. However, if the target is a pet, it will automatically be avoided. When attacking friendly monsters or shopkeepers (who do not attack characters), you will be asked "Are you sure you want to attack?" and you will need to respond with [y/n]. It is safe to proceed by entering y. Just remember that friendly monsters and shopkeepers should generally not be attacked.

Also, the effects and power of weapons can be found in the "Items" section, and the abilities of monsters can be found in the "Monsters" section. For other items such as altars, fountains, and sinks, and what meanings they hold, you can gain some knowledge by reading Sandras Fone's descriptions, who is considered one of the foremost experts on Yendor's dungeon.

42

CHARACTERS—The doppelgangers sent into the dungeon
SOURCE


## Page 045

To walk through the dungeon...

Commands

To travel through the world of NetHack, you must master numerous commands. However, most of them are single-key inputs, and at most two characters. You will naturally remember them as you progress.

The guildmaster took a seat at the desk in his private office and, as usual, put the tea to his lips. After taking a sip, he let out a small sigh.

"Today was the day to head to the dungeon... How many?"

He asked the woman standing by his side. It seemed like a routine conversation to them. His single word conveyed everything.

She pushed back her long hair and scanned the parchment in her hand.

"Four people came today. A Samurai, a Priestess, a Valkyrie, and a Thief each. None have come out yet. Only one person returned from the dungeon this morning. As expected, they didn't bring any amulet..."

After reading the report on the parchment in a businesslike manner, she paused slightly before addressing the guildmaster.

"But that's not unusual. When I entered, there were six of us — but there's still only one amulet."

Without looking away from the desk, the guildmaster replied. The quill in his hand moved smoothly across the documents.

"Why is that?"

The woman asked further.

"They must be puzzled too. Just like how we felt when we entered the dungeon." 

Commands Preface

43


## Page 046

Although she still held the feather pen, she looked up and replied.

"But if they are sufficiently wise, they should be able to escape the dungeon. With a bit of luck, they might even return with the amulet. Well, all we can do is wait for their return. We have entrusted them with everything we know about surviving in the dungeon."

"…That's right."

After a brief pause, she replied. She had taught her disciples all the survival techniques she knew in the dungeon. There was nothing else she or the leader could do but wait for their safe return.

She bowed to the leader and turned away, heading towards the door. She must pass on her skills to those aspiring to become adventurers like the four who entered the dungeon today.

Today was busy for her, just as it was for the guild leader.

Just as it was for her beloved disciples entering Yendor's dungeon.

In this chapter, I've explained each command by using situations to tell a little story. You should now understand the actions needed in various situations.

Note that when there is "t" after a Japanese word, it means to press the specified English letter while holding down the Ctrl key. When there is "#m" after a Japanese word, it means to first enter "#" and then the specified English letter. Please remember this clearly.

Also, although you will understand this as you play, commands have different meanings depending on whether they are capitalized or lowercase, so please pay attention to this.

44

COMMANDS—To walk through the dungeon...


## Page 047

; , Pick up fallen items

Nasrula raised her sword.

"Got it"

The greatsword thudded through the air with a loud noise as it fell.

The elf tried to block Nasrula's strike by holding her sword above her head, but her movement was too slow. Nasrula's slash bypassed the elf's defense and embedded itself in her left shoulder.

Blue blood wet Nasrula's cheek and armor.

"Oh, you"

The elf swung her retaliatory sword. But there was no strength left. She could easily parry with Nasrula's sword. A moment ago, she would have been sent flying against the dungeon wall just by blocking.

Nasrula parried the elf's sword and continued her counterattack. She added a powerful thrust, then swept her sword across horizontally.

"Ow"

The elf yelped. While she had avoided the direct hit, the tip of the sword grazed near her wound. Her previous movements were not what they used to be. The fluid, ever-changing sword technique was gone.

The fight was already over.

"Let's stop this"

Nasrula shouted.

"You have no chance of winning. It's pointless to fight."

"What's pointless? The battle isn't over yet. Even wounded, I won't fall to someone like you."

The elf repositioned her sword. The emerald green blade glinted faintly.

"I am a Dark Elf warrior and the leader of the Hyrpaion Knights, Neveryb. Can you surrender to a human?"

Wet from the blue blood soaking her upper body, Neveryb attacked. The sword was raised high above her head, aiming for Nasrula's head. It was an accurate strike. But N

Pick up fallen items

45


## Page 048

Sluura crouched down faster than the elf's sword could reach, slipping into her pocket. A white glowing sword severed the elf's right arm and pierced its heart, soaking more blood onto her chest than before.

"m, it's a shame"

The elf gasped for breath and knelt down.

"Defeated by a mere human, by a mere human. As a dark elf warrior, this should not have happened..."

Naslura swung her sword. Blood clung to the blade and splattered on the floor.

"Too... too much, you humans, you shouldn't be so arrogant."

The elf tried to speak but no words came out. His body folded over, unable to support his arms, as he fell. With a dull thud, the elf collapsed.

Naslura slowly approached. The elf's body rapidly lost heat, and the light of life was fading. The creature that had breathed, thought, and conversed just moments ago had become nothing more than armor and weapons.

"I forgive you," Naslura did not say. She had to achieve her goal at all costs. The dark elf had appeared to block her path and fought her. If he hadn't interfered, she would still be alive.

Suddenly, she stared at the elf's corpse. Alongside the sword, shield, helmet, and short sword, which were unfamiliar items, lay scattered. She bent down and picked up the short sword.

(No, maybe I was the one who was about to be killed.)

The dark elf was the strongest among the enemies she had fought in the dungeon. In terms of skill, stamina, and experience, he was superior. Naslura had won because he underestimated humans. If he hadn't thought of playing around, Naslura would not have had a single chance in ten.

She briefly gazed at the elf's corpse. Along with the sword, shield, helmet, and short sword, which were unfamiliar items, lay scattered. She bent down and picked up the short sword.

"This I will take. Master Elf."

She fastened the short sword to her belt.

She had no sympathy for the elf. A warrior must give their full effort even when fighting mice. To give only half the effort and lose is unacceptable for a warrior. He

46 COMMANDS—To walk through the dungeon...


## Page 049

He had lost as he deserved to.

But he took pride in being a warrior. The honor of a warrior was his life.

"Where should I send your keepsake? Give me your contact information."

He drew his sword and said this. It was the courtesy of a warrior to deliver the belongings of the defeated to the victor. Neverbi did not think he would lose, so he asked Nasrula about the whereabouts of the keepsake. He had no confidence in Nasrula, so he said nothing.

The result was the opposite. But he was a warrior.

Then, he would at least deliver the keepsake.

When you defeat a monster, sometimes a sword or scroll will drop along with the corpse. To check if there are any items that have dropped, use a command. Stand on top of the target item and press the (;) key. You can see the list of dropped items.

Checking and picking up dropped items

47


## Page 050

To pick up items on the floor, use the command. Just like when you did it before, stand on the item you want to pick up and press the ① key. If there is only one item, it can be picked up. When there are multiple items, you can select which one to pick up by pressing the ② or ③ key.

Picking up items is essential for progressing in the game. Valuable items often fall unexpectedly. Pick up the items you desire and try using them.

r

Read: 読む

On the cold floor of the dungeon, Tike lay naked.

The only thing covering Tike's body that couldn't be considered her own was a thin gown.

Her clothes, which she had been wearing, were piled high at her feet in a small mountain.

Through the smooth silk of the gown, the outline of Tike's body could faintly be seen.

"U...n..."

Tike took a weak breath and regained consciousness.

In the blink of an eye, she understood her situation and sat up.

"Ew..."

As her upper body rose, the gown slipped off her chest. Several rosy welts were visible from her collarbone down to her chest.

Tike tightly grabbed the gown and pulled it firmly to her chest.

"I..."

Tike's body was completely cold. It seemed as if she had been so warm just a little while ago, but her body remembered that this wasn't a dream.

48

COMMANDS—To walk through the dungeon...


## Page 051

Tike first experienced a thrilling sensation that made him shiver.

A fierce joy welled up from deep within his body and assaulted Tike's consciousness, compelling him to shout incomprehensible words without pause.

Suddenly, Tike threw away his robe.

He reached for the pile of clothes at his feet, but his gaze stopped on a spellbook lying beside them.

That's right.

When he was trying to memorize this spellbook, he came across it.

It was an Incubus, a humanoid monster.

While concentrating on memorizing a new spell, Tike did not notice the Incubus approaching from behind. Although all the doors in the room were closed, they had not been locked with Wizard's Lock. Most monsters would have noticed and retaliated after taking the first hit.

However, the Incubus did not attack Tike; instead, it enchanted him.

Tike obeyed its commands, discarding his weapon, removing his armor, and...

Biting his lip, Tike stood up.

Putting on the Hawaiian shirt silently, he picked up the bandaged mail from the floor. He felt strangely light. The paper inside the fortune cookie he had eaten earlier said, "The Incubus kills those it likes and grants power to those it likes more," and Tike wondered if that was true as he put on the armor.

Securing the shield to his left arm and placing the mace at his waist, he wanted to cleanse himself at the fountain, but there was something else he needed to do first.

Using a key, Tike locked both doors of the room. Then, he sat cross-legged on the floor and placed the partially read spellbook on his knees.

The cover of the spellbook was inscribed in gold letters:

"Finger of Death"

That Incubus must still be somewhere on this floor.

I will definitely find it and repay it with this spell.

Read

49


## Page 052

Commands are used to read scrolls and spellbooks. After entering the command followed by〔?〕, a list of your scrolls and spellbooks will be displayed, so it's useful to do so. As adventures progress into mid-game, you will always have several scrolls on hand.

When reading a scroll, its effects are immediately manifested. Unlike wands or rings, the effects of scrolls are often clearly visible, so even with unknown items, they are usually registered in the identification list displayed as〔〒〕. Scrolls that have not been identified are labeled with meaningless tags, but once identified, they change to meaningful names.

When attempting to read a spellbook, it takes some time until completion. During this period, monsters move around and attack, so it is better to learn spells in a closed space. If for any reason you stop reading halfway through, the spellbook will not disappear. There is no need to worry.

All spellbooks have a difficulty set equal to their level, which serves as a guideline for the required level to learn them (the spellbook level is the 'spell level'. 

50

COMMANDS—To walk the dungeon...


## Page 053

To convert experience levels, multiply by two and subtract one. For the best level 7 spell, it can be learned at experience level 13. In addition to that, the value of Intelligence is important, and characters with low Intelligence will have a hard time. If you try to learn high-level spells and fail, various (unpleasant) effects such as teleportation or being cursed may randomly occur.

Once a spell is learned, it is used by expending Pw equivalent to mana. After using it a few times, it becomes "out of charge," but if you read the same spell book again, you can use it once more. Think of a single spell book as being able to charge multiple uses.

---

Inventory Check

(Though, there's no time to dawdle...)

Nasrula descended the stairs and began checking her inventory. She had picked up quite a few items so far, but she hadn't had the time to sort them properly. Fortunately, the room she came down to has only one door, which is locked. Here, she can check her items before encountering any enemies and prepare herself thoroughly.

"First, the wands..."

Although their true nature is unknown, she has three wands. One is aluminum, one is iron, and one is oak. She could use them if she wanted to, but she cannot predict their effects. In the worst case, the power of the wands might be directed against herself. Holding a wand, she sees several burnt corpses. She is prepared to die, but she would rather die gracefully. She does not want to expose her face to the gnawing of rats.

"Next, four scrolls"

She arranges the scrolls tied around her waist. Two of them she had seen before. One is Remove Curse, a necessity for removing curses. It helped her when she accidentally put on a cursed armor previously. She has no intention of wearing a cursed armor again, but armor or weapons can sometimes be cursed by monster attacks. At least, having them will continue to help her in the future.

---

Inventory Check

51


## Page 054

Another is a scroll of charm. I haven't used it yet, but it seems to lower the combat will of monsters. It should be effective in rooms where there are swarms of monsters.

The other two are scrolls whose purpose is unknown. They might be cursed or blessed. What effects they have, Nasrula couldn't guess. Like the wand, using them directly was too dangerous.

(It's frustrating.)

The rest are rings and potions.

All the rings' identities have been revealed. It's a ring of fire resistance. With this, one can walk through fire. This was a valuable item for Nasrula, who is weak to heat. It was clear that a defensive ring would be advantageous during combat. The two rings are quite useful as one progresses in the adventure.

On the other hand, the potions were almost useless. Most of the potion identities remained unknown.

52

COMMANDS—To walk through the dungeon...


## Page 055

She sighed. She had confirmed that there was only one floating potion, but everything else remained unidentified. The liquids in the bottles were all vividly colored—red, blue, and green—but color did not necessarily correlate with effect. There was a possibility that some of them could be剧薬 or paralysis potions, which could be life-threatening.

(Nasrula thought to herself, "It's no use carrying such useless items, but")
she couldn't bring herself to discard them. If she could use a confirming spell, their true nature would become clear. Maybe there were useful potions among them.

(She felt a bit attached.)

With a sigh, Nasrula finally checked the remaining rations and weapons and armor. The armor was a new plate mail she had bought on the 6th floor, and it showed no signs of damage. The shield was the small shield she had brought down into the dungeon. Since magic power was sealed within it, its defense was high, but it seemed to have some scratches from overuse.

(Perhaps I should replace it soon.)

And the sword. It was the legendary blade Stormbringer, given to her by the god Loki who watched over her. Its sharpness was indeed excellent; it didn't even drip blood. For Nasrula, who lacked strength and stamina, Stormbringer was an indispensable weapon.

After confirming everything, Nasrula slowly stood up. Another enemy awaited her.

If you have many equipment and items, try using the i or I commands to check them. Both commands can be used at any time.

Press 1 to display a list of your possessions. The order will be amulet, weapon, armor, food, scroll, spellbook, ring, potion, wand, tool, jewel. If there are too many items to fit on one screen, press any key to switch to the next item.

The list will show the name and quantity of each item. For example, "2 uncursed

Checking Equipment

53


## Page 056

If "scrolls of enchant weapon" is displayed, it means you have two unencharmed enchant weapon scrolls.

The I command can display only the items you specify. Pressing ① and then a key will bring up a selection screen. Entering a symbol at this time will show a list of specific equipment or items. For example, entering ② would display a list of scrolls. If you enter ①, it will be staves, and if you enter ②, it will be scrolls. Additionally, entering "!" or "/" when using the I command will display the list without bringing up the selection screen.

There are special uses for the I command such as "lu," "lx," and "l$." "lu" shows items that are unpaid for, "lx" shows used items that are unpaid for, and "l$" counts money. This might be useful when you get confused about your purchases in a large shop.

D Drop 落とす

Nasrula felt her steps becoming heavier. It takes three to four steps' worth of effort to take one step. After ten steps, she starts to run out of breath, and every thirty steps, she needs to rest.

(Probably picked up too many treasures, huh?)

It's a compulsion; whenever she sees something that seems usable, she can't help but pick it up. As a result, mysterious potions and scrolls are stuck all over her body. She has sorted through them many times but still can't bring herself to throw them away.

However, if her inventory continues to grow, it will become a hindrance to her actions. In some cases, it could even affect her life.

"Guess I'll have to get rid of some."

First, she'll start with the gems. Nasrula had picked up quite a number of blue, red, green, and white gems. She doesn't know the names of these stones since she grew up in a world far from gemstones.

(If only Rapshee were here now.)

Nasrula was thinking of her friend from the training facility.

Rapshee, who shared the same room in the dormitory, is the closest friend among the daughters at the training facility.

54

COMMANDS—To walk through the dungeon...


## Page 057

She was very intelligent, always scoring top marks in written exams. She had extensive knowledge, especially regarding gems and potions, where she was unmatched even by teachers.

"Oh, that's a ruby. Don't handle it roughly."

"Uh, what about this one?"

"That's just a red glass ball."

Lapsy could name the gemstones just by glancing at them, and she never got it wrong.

"Why can you tell?"

Nasrula asked this many times, but Lapsy would only laugh and never answer.

For gem appraisal, fakes must be known, but genuine gems also require a keen eye. It's the ability to recognize the real thing that uncovers fakes, not the other way around.

Nasrula had a vague idea that Lapsy came from an upper-class background. However, Lapsy never revealed her past herself and showed no inclination to do so. Therefore, she did not ask about her background.

As friends, they spent much time together, learning about gems and potions...

But once inside the dungeon, appraising became a mystery. Even now, with several yellowish-brown stones in her hand, she couldn't tell if they were mere glass balls, topazes, or amber. If they were topazes or ambers, they could fetch quite a price at a specialty store. But if they were glass balls, they had no value at all, just clutter.

Nasrula hesitated.

But her decision was swift.

(There's no need to risk my life for items whose value is uncertain)

She threw all the gems away. Nasrula silently watched as the gems rolled away.

Next were the potions. She couldn't distinguish them either. Like Lapsy, she sniffed them, but couldn't differentiate them. They didn't make her drowsy either.

Drop

55


## Page 058

She also did not see any hallucinations.

In the end, the potions she had, aside from levitation and healing potions, were all unidentified items. She couldn't tell if they were potions or poisons. There is nothing more terrifying than unidentified potions. Although she had brought them to check equipment, it seemed they would just become part of her inventory.

(damn, am I going to throw this away too)

Nasrula left everything aside that she knew the identity of. If luck was on her side, she might be able to retrieve them later.

(if only I had asked Lapsy a bit more)

Looking at the mountain of piled-up gems and potions, Nasrula sighed. She felt ashamed. She thought such thoughts were unworthy of an adventurer.

However, it was true that it was a pity.

56

COMMANDS—To walk through the dungeon...


## Page 059

If you have too many items and equipment to carry anymore, it might be better to use the d or D commands to drop some items.

If you know which item you want to drop, type "dh" followed by the letter of the item in your inventory. Typing "dh 2" will drop two of that item. If you don't know which item to drop, just press (d). When asked what to drop, pressing (?) will show you a list of your items so you can carefully examine them before deciding.

The D command allows you to drop multiple items at once. Pressing (D) will ask you what to drop. Here, you can input a symbol to specify which item to drop. Entering (/) will drop wands, and entering (?) will drop scrolls. You can then choose the items you want to drop by looking at the screen. This command is handy when you want to drop a specific set of items all at once.

There are special uses for the D command: "Da" and "Du". "Da" drops all items without confirmation, while "Du" drops items that haven't been paid for. Using "D ? u" will allow you to drop only unpaid scrolls. These commands can be useful in shops.

---

Opening, Closing Doors

Nasrula closed the door.

(I saw something unbelievable)

Behind the door was a monster. Not just one or two, but a room barely large enough to hold an overflowing number of monsters. 15... no, it could be as many as 20.

"There are rooms in the dungeon where monsters gather."

Nealco Sensei taught during a lecture.

"This place is dangerous. Even if you can fight each monster for more than five minutes individually, against a group, it's impossible. The strength of the monsters can double or triple."

"..."

"If you fight properly, you'll be turned into meat in less than a minute."

Door Opening, Closing

57


## Page 060

"Then what should I do?"

When Nasrula asked, Nearchus smiled faintly.

"Already decided."

"..."

"You run away."

Nasrula turned her back to the door. She intended to follow her master's words faithfully.

However, her feet did not move.

Certainly, if they fought normally, they would not be able to defeat the enemy.

(but, if we launch a surprise attack, it might work)

The monster has not noticed that Nasrula opened the door. Fortunately, she still had one more use of the wand of fire. She also had a ring of protection. If she could take down one-third of them before they were ready, and face them at the entrance... Even if she couldn't come out unscathed, she should be able to fight evenly.

She had undergone surprise attack training multiple times at the training facility. In the surprise attack course, Nasrula had received a grade of "Excellent." She would approach and attack the opponent unnoticed by her comrades. The opponent wouldn't even realize they were found until they were defeated. She had once managed to kill nearly twenty trainees in a mock battle alone. She was confident.

(but, shall I do it?)

Nasrula had bought quite a bit of food on the 8th floor underground, so she wasn't financially strained. However, she no longer had the funds to buy armor or scrolls.

It was said that there was a large amount of money in the room where monsters gathered, taken from adventurers. She wanted to save up for future adventures. The best way to get money was to find a treasure chest, but without teleport scrolls or magic maps, it was difficult in her current situation.

While this room where monsters gather was not the best option for making money, it was still a second-best choice.

(but...)

Nasrula hesitated to put her hand on the handle.

"Avoiding danger as much as possible is a fundamental rule for adventurers," Nearchus often repeated. One shouldn't risk their life for short-term gains. It may seem like a detour, but it's sure.

58

COMMANDS—To walk through the dungeon...
SOURCE


## Page 061

It is safer to follow the safe path. It's too late once you die, and everything becomes slow.

Nasrula's funds are tight, but it's not something that would be life or death. It seems foolish to risk one's life just for a scroll.

(Here, be honest)

her rationality was telling her.

She hesitated. Her thoughts raced back and forth, oscillating between conflicting choices. She couldn't seem to settle down.

Should she open it or not? That was the question.

However, Nasrula's scales tend to tip towards emotion rather than reason.

Moreover, her blood was that of an adventurer. She knew danger was involved. But if she were to avoid danger at all costs, the adventure wouldn't progress. Most importantly, she was afraid of danger.

Door opening and closing

59


## Page 062

She, however, does not enter the dungeon from the beginning.

(This is a trial)

Nasrula thinks.

(If I cannot break through here, I will not be able to survive in the future)

She touches the door.

Taking a deep breath, she opens the door.

The monsters' gazes converge on Nasrula as she jumps into the room. A strange scream rises, and the monsters sitting on chairs stand up. An orc wields a sword and intimidates her.

Nasrula raises the flame wand. The wand glows crimson.

"Go ahead!"

Flames writhing like snakes burn the monsters. Screams echo through the room, and a foul smell assaults the nose. Corpses roll like wood and disintegrate.

Even though there is a room in front of her, she cannot enter or advance. This is because she has not opened the room's door. To open the door, you need to press key ① and specify the direction of the door. When the door opens, a message appears, and you can freely enter and exit.

Usually, it opens with one try, but if the door is poorly made, it may not open easily. In that case, try several times. By the third or fourth attempt, if the key is not engaged, it should open.

A door with a key needs to have the key removed first. There is a high chance that your effort to open it will be in vain without a key. It would be better to stop or find another way to open it.

To close an opened door, press key ③ and specify the direction of the door. The door will close, and you will no longer be able to enter or leave the room. Although this is used less frequently than opening a door, it is effective when escaping from a monster without hands. Please try it when you feel it's dangerous.

60

COMMANDS—To walk through the dungeon...


## Page 063

Spell Casting 咒文詠唱

"Hey?"

Yoshitane couldn't help but stare at his hands. The hands that were supposed to be holding a katana were now empty.

However, upon checking his entire body, it was not just the katana that had disappeared. His helmet, dragon hand gauntlets, and even the plate mail he had struggled to obtain, made of crystal, were also gone. The only remaining piece of armor was a pair of boots reaching up to his knees. Even his backpack felt lighter.

"Damn, so... I met a nymph."

Slumping onto the floor, Yoshitane let out a sigh. A look of regret, one that could not be fully expressed in words, appeared on his face.

Nymphs—endlessly praised by countless sculptures, paintings, and poems for their beauty. Even the most beautiful women, who have polished and honed their beauty to its utmost limit, would find themselves unable to match the nymph's allure. Her beauty is beyond description, and no sculpture, painting, or poem can compare to it.

She was that beautiful.

Yoshitane was captivated by her mere appearance. He could not even move an eyebrow, and he allowed the mischievous nymph to take his katana, remove his helmet, and even pull the dragon hand gauntlets off his arms. No, he had no choice but to allow it.

"Huff"

Yoshitane took a deep breath.

"I need to check what was stolen..."

Muttering this familiar phrase since entering this magic dungeon, he rummaged through the contents of his backpack.


## Page 064

And then, his eyes widened in disbelief. There was not a single weapon to be found. Even his trusted Thunderbolt Wand and a single shuriken were missing.

"Whaddya know?"

Yoshitane couldn't help but look up at the sky. Since he needed to defeat a Nymph to retrieve what was stolen, he now found himself fighting bare-handed.

At that moment——a Nymph appeared in the room where Yoshitane was.

With the power to transcend space, the Nymphs appeared and disappeared at will. With a beautiful and alluring smile on her face, she seemed to be closing in on Yoshitane once again...

"Damn, if there's nothing..."

Even though the distance was still great, Yoshitane was not yet entranced. However, once her naked body pressed against his, his mind went blank in an instant.

"Piss off, I'll give it a try."

He knew that only one option remained for him. But it was a hand that lacked certainty. Yet, it was the only hand he had left.

62

COMMANDS—To walk through the dungeon...


## Page 065

It is also a fact that there are things that cannot be prepared for.

Yoshitane, having made up his mind, closed his eyes and placed his right index finger on his forehead. Strange words leaked from his lips. As he continued to chant, he immediately felt a hot mass rising from within his body.

Opening his eyes, he saw the nymph approaching him. The nymph seemed suspicious of Yoshitane's actions, and her steps were slightly delayed. However, Yoshitane did not stop chanting.

He turned his hand over and raised it high. When the chanting stopped, a roar unlike any shout or battle cry came from Yoshitane's mouth. At that instant, his fingertips firmly grasped the nymph. Several beams of light shot out from his fingertips.

The stream of light tore through the sky and was absorbed by the nymph's body.

The nymph let out an inaudible scream and fell to the ground.

From somewhere on her body, pieces of armor and dragon scales began to fall off.

"Haha. It's done..."

Yoshitane slumped to his knees. The unfamiliar incantation and the concentration required had unexpectedly drained his energy.

"I'd rather not do this again."

Breathing heavily, he muttered to himself while repeating the spell in his mind.

"Magic missile. Might come in handy depending on the situation."

By reading a magic book, spells can be memorized and used with the Z command. The list of memorized spells can be displayed using (x) or (+).

Each time a spell is cast, the memory of the spell fades (chanting a spell consumes the memory of the spell). In some cases, the spell may even be forgotten entirely.

When casting certain spells, input is required for the direction of the spell. For offensive spells like magic missiles, use the movement key in the direction of the enemy. To cast a spell on yourself, press (○). It is also good to remember that light-based spells will reflect off walls.

However, if intelligence is insufficient or if there is not enough energy to cast the spell,

Spell Chanting

63


## Page 066

If there were no items or sufficient power (Pw), nothing would happen, and power would be wasted only. It is safer to do a test strike (though it might be called something else) before using it.

Apply Tool to use

Nasrula felt the world turn upside down. He lost strength in his legs and bent at the knees. When he tried to put his hands on the ground, he could not move them and lost balance. Nasrula fell on his back, and his vision became distorted. His sense of balance was off.

He was careless. He had checked everything, but apparently, some strange food had mixed in.

His limbs began to spasm, and he could not move freely. His vision remained distorted, and he heard ringing in his ears.

However, fortunately, his thoughts were clear. The degree of corruption was low. It didn't seem like he had received fatal damage.

(If I had just lain on my side a little...)

Nasrula thought. More accurately, there was nothing else he could do.

(If a monster came, it would be hopeless.)

He intended to laugh, but even his lips wouldn't move.

He felt nauseous. This was the feeling he had after drinking too much alcohol during his training days, two days after getting drunk for the first time. At that time, he did not know where his limit was. He got drunk on the atmosphere, and even Rify and Lapsy could not stop him from opening two bottles of wine. The next day, he could not move and lay on his back without moving.

It will take quite some time to recover. His senses were going haywire, screaming in agony.

The flickering vision stabilized, and the outlines of objects became clear. The high-pitched groan gradually subsided, and silence should have come... but Nasrula's ears caught something.

(Something is here)

64

Commands—To walk through the dungeon...


## Page 067

In a large dungeon, it's unlikely to encounter other adventurers except Nasrula. The sound of footsteps was clearly those of monsters, and they were quite close. They might be in the same room, or even if they are far apart, there would be no more than a wall separating them.

I tried to utter some taunting words, but my voice failed me.

(This is bad, I can't even use the unicorn's horn)

The unicorn horn is a magical item. It can remove all sorts of ailments, hallucinations, blindness, and any hindrance. With the unicorn horn alone, one could recover from any condition to full health.

However, my limbs were still not free. Straining to put strength into my arms, I could only feel the tips of my fingers moving slightly. Though the unicorn horn was just a short distance away at my waist, it felt as though a diamond wall had formed, allowing only my fingers to move.

The roar of the monster was getting closer and closer. There is no doubt that they are in the same room now.

(Hurry... use the unicorn horn)

Use tool

65


## Page 068

Nasrula moved her fingers by instinct.

She felt the texture of a bottle of medicine at the tip of her finger. The unicorn's horn was beneath it.

But that was as far as it went. Nasrula could no longer move her fingers. The monster was looking down at her.

The true identity of the monster was unknown. But even if it were the weakest monster, it would be a formidable opponent for her now.

(That's it so far)

She had made up her mind.

However, to her surprise, there was no attack. Most monsters would not hesitate to attack an adventurer the moment they spot one. Whether with a sword or fangs, there was never any hesitation.

(Maybe...)

The monster might be hesitating. It might think she was already dead, like a jackal that feeds on corpses. Monsters that feed on corpses do not attack corpses. And certainly not intelligent creatures like elves...

Nasrula did not move her body at all. Her breathing, as well as every muscle in her body, was completely still. She was pretending to be dead by not moving.

Nasrula's gamble paid off. The monster had been watching her for a while but eventually left.

Once again, Nasrula moved her fingers. She felt something hard against the tip of her finger.

(This is it)

She reflexively grabbed it and pulled it out with all her strength. She forcibly lifted the arm that tried to resist and held it to her forehead. Because her sense of touch was incomplete, the tip of the horn had pierced her finger. She realized how severe the numbness was because she felt no pain. However, what she pulled out was undoubtedly the unicorn's horn.

Nasrula felt the numbness being sucked away from the unicorn's horn. At the same time, her sense of pain returned to her fingers.

(We can do this)

She grasped her sword and stood up. The monster turned around and stared at her.

66

COMMANDS——To walk through the dungeon...


## Page 069

It was as expected, an elf.

Nasrula readied her sword and faced the monster.

a is a command to use an item.

Items are objects categorized as tools. There are many kinds, such as unicorn horn, blindfold, pickaxe, lamp, key, etc. They can be used by pressing the 'a' key. When opening a door, press the 'a' key to select the key and specify the direction of the door you want to open. As long as you have the key, you can unlock it.

When using a pickaxe, press the 'a' key and specify the direction of the wall or door you want to break. A blindfold can be used by pressing the 'a' key and selecting blindfold, which will block your vision and put you in a state similar to blindness. It is essential when fighting monsters that petrify upon eye contact.

Using these items is almost impossible to continue adventuring without them. I hope you will choose tools wisely and overcome crises.

Z

Zap wand

"Ah!"

Yoshitsune let out a small cry.

He entered an unknown room, but was caught off guard and attacked immediately.

However, he managed to parry the attack... or so he thought. He had struck down the enemy with one blow. His swordsmanship was worthy of praise. ...That is, if the opponent was not an Acid Blob.

An Acid Blob is a magical creature armed with strong acid for self-defense. When you slash at it with a sword or axe, the acid damages the blade deep inside its body. Yoshitsune always tried to fight Acid Blobs with kicks or bare hands. At one point, he even had a club endorsed by the shopkeeper for its resistance to acid, specifically for fighting Acid Blobs.

However, there was no time to switch to bare hands or kick in for the current surprise attack.

Wand zap

67


## Page 070

There was nothing at all. The body reacted before any such thoughts could arise. It's something that would be praised for a warrior.

"…It depends on the situation..."

Yoshitane muttered as he gazed at the katana he had long cherished.

A stimulating smell of acid and smoke unique to when metal dissolves in acid wafted from the katana. At least, there must be several spots where the blade has chipped. But if he tried to wipe it off, he might end up burning himself. There was nothing Yoshitane could do but watch silently.

Several hours later, the smoke finally subsided. When he lightly swung the katana back and forth to check its balance, it was clear that the center of gravity had changed. Even ignoring the issue of chipped blades, it would be difficult to hit an enemy with it.

"…I need to enchant it with a scroll... it won't work..."

Yoshitane sighed and sheathed the katana, drawing his sidearm instead. A chipped katana was better than nothing, even if it was just a regular short sword.

At that moment, Yoshitane noticed a growl coming from the other side of the door.

(It's an oak.)

And it seemed to be the worst Uruk-hai. Just moments ago, Yoshitane had encountered several Uruk-hais on the floor above, and they had left him half-dead.

(The disgusting breath, I can't forget it even if I wanted to...)

Yoshitane glanced at the Thunderwand at his waist—revealed by his mistake. The wand, which releases powerful lightning by unleashing trapped magical power, might have already lost all its magical power.

(...How many more times—no, how many times can I still use it?)

Just as he thought this, the door opened. In the darkness, five Uruk-hais were visible. Yoshitane reflexively drew the wand from its holder and swung it.

The wand burned in Yoshitane's palm.

Two large flashes of light erupted.

When the flashes subsided, the room was left with four corpses and one Uruk-hai that was half-burnt to charcoal.

68 COMMANDS——To walk through the dungeon...


## Page 071

YoshiTune threw away the wand and held the wakizashi straight. He intends to stab the wounded Uruk-hai with it. After that, he might be able to eat the meat of the oak that has been roasted to an appropriate degree. It probably won't be a refined taste, though.

During your adventure, you can use the wand by entering the z command. If you have multiple wands, you can input 1 to see what kind of wand you have. However, just like other items, the nature of a wand obtained immediately after is unknown. After all, there is even a wand with "no power at all."

It would be better to identify it as a scroll or spell before using it, but you can also identify it by swinging it at a monster. If fire comes out, it's a fire wand, and if lightning comes out, it's a lightning wand.

However, the light emitted by many attack-type wands will reflect off walls. Of course, don't try to use it against a wall in a narrow room.

Waving the wand

69


## Page 072

Of course, one more sacrifice will be added (who that sacrifice might be... this is also needless to say). It would be better to avoid using attack-type wands unless there is a spacious area.

Other 'convenient' wands should be a great help in your adventure. By the way, if you want to use a wand on yourself, just input when asked for direction.

However, all wands have a 'usage count' set. The number in parentheses when listed with the i command indicates the usage count. When this becomes zero, the wand runs out of power and can no longer be used. Wands that are unidentified may not react at all when their power is known but the usage count is unknown, rendering them useless.

Moreover, cursed wands have the weakness of potentially exploding along with their normal effects.

In this way, while wands are convenient, they come with dangers when used. However, if you properly identify them and use them in the right place and situation, they will be very helpful.

S

Searching the Dungeon

The path ended here.

Nasrula examined her handmade map. Calculating from the steps, there must be a room beyond the wall.

However, what stands before her is merely a stone wall; no door is visible. "There must be a secret passage somewhere..."

She ran her hand over the wall, but there was no reaction. She prodded it with the tip of her sword, but no change was observed. Upon rechecking, the result remained the same.

Nasrula bit her lip.

"Dead end...?"

If there is no door here, she will have to return the same way. But, if she takes a few steps, she will encounter an ogre. At her current level, she could not defeat that monster. Earlier

70

COMMANDS—To walk through the dungeon...
SOURCE


## Page 073

She had been on the verge of being killed. In her current state where her wounds had not yet healed, it was clear that she would become an ogre's meal.

She faced the wall.

"Are you going to give up?"

Nasrula remembered the words of Nealko the Master.

Nealko the Master had explored many uncharted lands as an adventurer, including the Sea of Chaos, and achieved great success in adventurer education even after retirement. Countless famous adventurers such as Narktik who explored Eclipso Mountain and L'Yorlachien Ranger who revealed the full extent of the Farmandon Caverns were among his disciples.

He was also Nasrula's mentor at the adventurer training school. Nealko the Master taught Nasrula the skills necessary for an adventurer. The techniques he taught were perfectly useful in the dungeon. In fact, without his techniques, it would have been impossible to survive in the dungeon.

That man gave a final lecture to all graduates before their graduation.

"Do not give up."

Nealko the Master peered into the eyes of his disciples.

"In the dungeon, those who give up lose. Whether your stamina is low or you are surrounded by monsters and at a dead end, you must not give up."

"Master!"

Nasrula raised her hand. Her companions frowned and stared at Nasrula. It was the greatest disrespect to interrupt a teacher's speech in the training school. Some teachers might even hit the student who interrupted. However, Nealko the Master merely chuckled slightly.

"What is it?"

"I have a question."

"Go ahead."

"I agree with what you said about not giving up. But there are times when it truly seems impossible. For example, when surrounded by monsters on all sides with no escape route, or when fighting is futile. What should one do in such situations? Should one really give up?"

Dungeon Exploration

71


## Page 074

Is it better if it isn't there? Perhaps it would be better to die cleanly without making such a spectacle of oneself.

Nealco the Master looked at Nasrula for a while. There was no anger in his gaze. Instead, it was a gaze filled with compassion, similar to that of a father.

"Perhaps that might be true."

Nealco the Master said almost to himself.

"However, I cannot advise you to do so. What I have taught you and your companions is the skill to survive. I have trained you all to endure any environment and return to your families and friends here. I cannot advise you to die."

"Then what should we do when we find ourselves in a hopeless situation? What should we do when there is no escape, when our food runs out?"

"Act."

Nealco the Master looked straight into Nasrula's eyes and firmly declared.

72

COMMANDS—To walk through the dungeon...
SOURCE


## Page 075

"Even if it seems reckless, that's fine. Even crazy actions are acceptable. There's no need to think calmly. Move forward. Just keep moving forward. Then a way out will open up."

Nasrula listened silently. She wanted to argue but couldn't find the words.

"You don't have to understand now. You'll understand after you've had some adventures."

Nasrula nodded at Nealko's words.

At that time, she couldn't understand it. It was a lie to say she wasn't afraid of death. But she didn't want to die in a pathetic manner.

However, after descending into the real dungeon, her way of thinking changed. She no longer wanted to die. She didn't know why, but as she saw the bones of those who died unseen in the dark dungeon, she became afraid. She didn't want to be like that. She desperately wanted to survive and get back to the surface.

Attachment grew in Nasrula's heart.

"Are you going to give up?"

Nasrula muttered and began checking the walls. She broke apart bricks, dug through mud, and meticulously checked to see if anything was missed.

She found the handle of the hidden door just a few hours later.

When stairs cannot be found in Yendor's dungeon or when there's a message but no shop is found, it's likely that hidden doors or secret passages were overlooked.

In such cases, use the 's' command. Press the 's' key in places where a door or passage might be hidden. Often, it won't be found on the first try, so try the 's' command again wherever you think it might be. Typing "n 10 s" will allow you to explore 10 times in a row.

Additionally, elves automatically check walls and passages without needing to input the 's' command. They possess a superhuman ability to discern slight differences in walls and passages. However, they are not infallible, so don't overtrust them. If something seems suspicious, use the 's' command. Only elves are born with this exploration ability, but archaeologists, thieves, and (for some reason) tourists can develop similar skills through experience.

Dungeon Exploration

73


## Page 076

Sometimes doors and passages are cleverly hidden by location. Don't give up, and search thoroughly several times. Unforeseen good fortune may await you.

# o # p

Offer, Pray - 捧げる、祈る

"Wow, it's heavy..."

Tike was panting as he carried a corpse that weighed almost twice his own body. It was one of the Frost Giants he had killed in the nearby room. There was no way to lift and carry it, so he dragged it by one arm over his shoulder. He took each step slowly, pressing down with each foot.

Tike wasn't going to eat this. He intended to take it to the 'Altar Room' he found on this level.

There, an altar dedicated to the god Crom, whom Tike serves, stands.

If Tike were a Priest and had taken another profession, he could have simply ignored it and walked past. Or if it were a Lawful or Chaotic god, or even a Neutral god other than Crom...

From the style, Tike knew without a doubt that this altar belonged to Crom. No, he knew it. He had seen it every day for years. There was no chance of mistaking it.

Tike cleaned the dilapidated altar and wandered around seeking offerings to present to Crom.

Fortunately, the Giants' lair was on the same level. Tike's strength had grown to the point where he could easily deal with Giants. If he returned to the surface, he would be given the title Canon. The armor he wore was made from scales taken from the Gray Dragon he had defeated earlier, and his sword was none other than Excalibur.

By offering this Giant's corpse, Tike's service would likely come to an end. A Giant of such size should surely satisfy the god.

Still... 

74

Commands—To walk through the dungeon...


## Page 077

"Quite heavy, huh! What if I just left this giant and ran away!"

Tike stopped to think about what would happen if he abandoned this giant and fled. Croth would surely be angry and wouldn't lend him a hand again.

"Um... sir, siiigh... six times, maybe?"

Tike recalled how much Croth had helped him until now. When he was still in a shallow level of the maze, on the brink of starvation. When the Coctritus's petrifying poison had spread throughout his body and he was on the verge of losing consciousness, calling out to Croth for help. When he was surrounded by Minotaurs and recovered his strength with Croth's power. There were also times when he prayed to remove a cursed ring or for trivial matters.

"But I have to do at least this much... Ugh! It's so heavy!"

Tike gathered his resolve and started moving again. 

Offer, Pray


## Page 078

Several minutes passed, and Tike was between the altars. Struggling to place the giant's corpse on the altar, Tike fell onto the floor, panting heavily like a horse that had run too far and was about to collapse. After resting for a few minutes, Tike finally managed to sit up, mumbling prayer words with a look of reluctance.

"O Crom, lord of this world's battles and swords. Accept this offering as a token of my gratitude..."

At the end of his sentence, he raised both hands above his head.

"...What?..."

After waiting for a while, nothing happened. Normally, the sacrifice should vanish instantly.

"Um, excuse me... Crom?"

As Tike began to wonder whether he had made a mistake in his prayer or if he had fallen asleep at the altar, a loud "Old man!!" echoed in his mind.

"Sorry! Sorry!"

Tike clutched his head and desperately shouted.

The giant's corpse had apparently deteriorated since it was brought here.

Tike had noticed a strange smell and suspected it might be in poor condition.

The #p and #o commands are both related to gods. However, one would not typically use the #o command unless they had found an altar. The #p command is more commonly used.

Praying with the #p command can sometimes resolve various issues. These may include hunger, a critical loss of hit points, blindness, paralysis, or cursed equipment. If you find yourself in a difficult situation during the game, try praying first. Whether your prayer is answered depends on your wisdom value. However, if the god is angry or enough time has not passed since your last prayer, help will not be forthcoming. Additionally, if you are on what is called the 'hell' level, divine power cannot reach you.


## Page 079

Praying without need will anger the gods and bring down their punishment upon you.

Standing on the altar and using #0, you can offer the corpse of a monster. As long as it is your believed god's altar, it does not matter where it is (the name of the god can be found by using the command on the altar). The greater the monster you offer, the greater the reward. A raging god may calm his anger, and if you have a friendly relationship with him, he might grant you some powerful item. However, since altars that appear in the dungeon are random, there may not be an altar corresponding to your attributes.

q

Quaff Drink

"Kya!"

The moment TiKe opened the door and entered the room, she let out a scream.

However, this was not because of the familiar, horrifying monsters that had become accustomed to during dungeon exploration, nor was it due to a malicious trap whose nature could be discerned from the character of the setter.

There was a "spring" in that room. In this case, the scream was one of joy.

"Kya kya!"

TiKe, jumping around excitedly near the spring, had completely forgotten to be cautious of her surroundings.

It seems the water accumulated in a depression on the floor, seeping from the ceiling, reaching about knee-deep. TiKe knelt on the floor and peered into the water. The clear water reflected her face like a mirror.

(Yikes! So dirty... This looks like a beggar!)

Five days had passed since TiKe entered "Yendor's Dungeon." After battling monster spit, dust, oozes' slime, and spider webs, TiKe's entire body was soiled—unfit for public display, especially as a teenage girl. The robe given by the High Priest before departure now emitted an unpleasant odor at various spots.

Drink

77


## Page 080

There are stains.

Tike stood up and began to remove each of the items he was wearing one by one.

He finally found a spring where he could bathe. There were a few on the floor above, but they were polluted with the bodies of orcs and had a terrible smell.

The chain mail that had been removed fell with a thud at his feet.

Holding one hand over his still-growing chest, Tike tried to step into the spring with his toes.

"Ah... and!"

At the point where his foot touched the water, Tike exclaimed and stopped himself from entering. His desire to bathe was so strong that he had forgotten something important.

"My throat was also parched."

It's clear which should come first: washing his body or drinking water. Tike scooped some cold water with his hand and brought it to his mouth.

At that moment, the water in the spring started to move.

The water gathered in the center of the spring and gradually rose, forming a vortex.

The "water" took on a humanoid form and eventually transformed into the shape of a demon with two arms and a pair of horns.

"Aa, aa..."

Tike was so taken aback by the sudden event that he couldn't even stand up, let alone retreat.

"Did you summon me?"

The demon's pronunciation was somewhat archaic, but its words were understandable to Tike.

"Um, um! S-sorry! I...!"

The demon continued without paying attention to Tike.

"By the ancient pact, I am... "

"Please! Don't kill me!!"

"... By the ancient pact, I can hear one wish of yours."

78

COMMANDS—To walk through the dungeon...


## Page 081

"Ah?"

Tike blinked his eyes.

"Your wish has been granted. I should thank you for freeing me"

Steam-like substance began to emit from his body, and the demon gradually shrunk.

After a while, Tike, still dazed, muttered,

"I must have missed my bath..."

The q command is used to drink something. It can be used for potions or for the water of a spring represented by {. To drink the water of a spring, stand on it and input the command. However, be careful as the left parenthesis, }, represents digging, which can lead to certain death if entered. It's better to check beforehand using the / command.

Also, when drinking a potion, its effects will manifest immediately regardless of what it is. The quickest way to identify an unknown potion is to drink it. However, there are potions that can cause blindness or paralysis, among other unwelcome effects. You need to be prepared for such possibilities. Drink


## Page 082

Once the effect of a potion has been determined by using it, it is added to the identification list that appears with the identify command, and any potions of the same color found subsequently will automatically display their names.

When drinking water from a spring, various effects may randomly appear. While it often just quenches your thirst, you might receive a small nutritional boost, or conversely, have your strength drained by the poison in the water. In very rare cases, a Water Demon or Water Nymph, creatures of the water, may be summoned. If a Water Demon appears and you happen to be blessed with a handful of good fortune, he (or she) might grant your wish.

But seeking luck through random sips of spring water can be considered a foolish act. The scales of fortune and misfortune are balanced in the effects of the spring. You might carry a fatal misfortune before encountering any good fortune.

---

Up, Down: Stair Climbing

Nasrula carried several unidentified staves in her left arm as she stepped onto the stairs. Since they were made of stone, they wouldn't break easily, but the near-vertical descent was terrifying. Trembling, she clutched the pillar with her free right hand.

She carefully and slowly descended one step at a time. With each step, the floor of the lower level came into view. If she had nothing else, she could jump down from here. However, three bottles in her pocket caught her attention. If the bottles broke and the contents were absorbed, she couldn't predict what would happen. There was even a possibility of going blind instantly.

Her steps naturally slowed as she descended the stairs.

(Such a pathetic sight.)

Nasrula thought to herself.

(What would he (or she) say if he (or she) saw this?)

Nasrula imagined the faces of her training school friends.

80

COMMANDS—To Walk Through the Dungeon...
SOURCE


## Page 083

Nastrula hears a shout of anger as her classmate Riffor yells down the stairs.

It was Riffor. He was looking down at Nastrula from the training stairs.

"Look down, close your eyes and jump. It's not that high, so there's no need to worry."

"Can't be that easy."

"Well then, you don't have the talent. Maybe it's better if you give up adventuring and find a good man somewhere."

"Shut up."

Nastrula carefully checks her footing and slowly steps down.

"Oh, no way. Seriously, get out of the way, I'll show you how it's done."

"It's fine. I'm doing it my way. You remember, you had a challenge, right? Spell reading. I did that."

Riffor's face changes. He twists his mouth and sticks out his tongue.

Nastrula thought to herself.

(I won.)

As expected, Riffor disappeared above her head.

(It's not a joke. Training with a guy like that... )

Nastrula knew she would only sink into self-loathing. Riffor would descend the stairs in half the time it took her. No one could match her in lightness.

Riffor was an extremely talented trainee, but he was shunned by the students.

The reason was simple. He came from a thief background.

The training school gathered students from all social classes. The most common were children of adventurers like Nastrula, but there were also farmers, craftsmen, merchants, knights, samurai, priests, and wizards.

Among them, Riffor was unique. A thief trainee like Riffor

Stair climbing

81


## Page 084

In addition to them, there were a few others, but all of them were lying about their origins. They were careful not to let anyone know that they were thieves. But Riefu was different. He clearly announced during self-introduction that he was a thief, and even said that he was proud of it.

Nasrula knew how thieves were regarded outside the training facility. There were very few students who would be willing to associate with a student who openly declared that they were proud of being a thief. Nasrula was one of the rare exceptions.

Nasrula and Riefu had a strange rapport. The skills she learned were countless. How to open boxes, how to disarm traps, and her dexterity were almost entirely based on his teachings. She passed the exams thanks to Riefu's help, despite being clumsy.

Why he is avoided, Nasrula could not understand. Riefu is an honest man who does not lie. He is not one of those worthless fellows who try to cover up with empty talk. He is a trustworthy man.

82

COMMANDS——To walk through the dungeon...


## Page 085

(Well, let's continue with the training)

Nasrula started descending the stairs. She followed the tips he had given her on climbing and descending. Finally, Nasrula reached the ground.

When she felt the texture of the ground, she felt as if she were ascending to heaven despite having descended. Thinking that she could no longer fall, Nasrula took a deep breath and sat down on the ground.

"Good job"

After each training session, the man would always call out to her and give her advice.

Even now, it seemed to Nasrula as if she could hear a man's voice from somewhere.

Using stairs is a necessary action to conquer the dungeon.

To use stairs, you first need to find them. Usually, ascending stairs are indicated within the dungeon, while descending stairs are shown by the ">" symbol. When the symbol is not visible, try walking around the statues. There is a possibility that they are hidden beneath the statues.

To ascend or descend, move your character to the symbol and press the same key. The screen should then switch, and you should be able to confirm whether you are on the upper or lower level.

Just carrying too many items can result in being unable to use the stairs and having to reluctantly drop some items. When using stairs, pay attention to both your items and your carrying capacity. Also, if you do not have Yendor's amulet and attempt to use a stair leading to a higher level from level I, the game will end, so be careful.

As the adventure progresses, other means of moving between levels will also appear. However, the basic method remains using stairs, and it is impossible to achieve your goal without using stairs. Once you arrive at a new floor, make sure to secure the downward stairs first.

Stair Ascending and Descending

83


## Page 086

Put on, Weild, Wear 指輪装着, 武器装備, 防具着衣

When she took off her plate mail, there was a new armor in front of her. It was a pale gray color. The impression was far from good. It was made entirely of leather, with no metal used. Even if it were in a specialty store, there wouldn't be a single person who would want to buy it. It was a plain-looking armor.

However, she knew. She knew it was a dragon's armor. It was stronger than any other armor and rich in defensive power.

"Have you heard of the dragon's armor?"

It was three days before entering the dungeon that her uncle spoke to her.

At that time, Nasrula had returned to her aunt and uncle's home. She had informed them in advance that she was about to embark on an adventure. However, she wanted to tell them herself that she was going to the dungeon and express her gratitude for raising her.

But in front of her weeping aunt, she couldn't say anything. Her aunt was a strong woman. Nasrula had never seen her cry since being taken in, not even when her aunt's brother died and the funeral arrangements were made on the battlefield. She was called "the Iron Woman" behind her back.

Nasrula could hardly believe her aunt crying like a child. She didn't know what to do and just stood there in a daze. She might have stood there until morning if her uncle hadn't put her aunt to bed.

"Anyone can't stay calm when their own daughter goes on an adventure. It's different from getting married. The possibility of never seeing each other again is higher."

Nasrula listened silently to her uncle's words.

"..."

"Still, you want to go, right?"

Nasrula nodded.

"Then listen to me one thing. Don't think I'm trying to manipulate you," he said, then asked Nasrula if she knew about the dragon's armor.

84

COMMANDS—To walk through the dungeon...


## Page 087

Nasrula shook her head. It was something not taught at the training facility.

"Dragon armor is armor made from dragon scales. It's much harder than ordinary armor. You can't even scratch it with most weapons. It's the strongest armor."

"I didn't know that."

Nasrula muttered.

"The training facility didn't tell us."

"Of course not. Few have seen dragon armor. In ancient times, only a few such as the Prophet King Bialy, Ring King Gudorfin, Sir Eclipse, Sir Saint Simon, and Sir Hyperion."

"So why does my uncle know about it?"

Nasrula stared at her uncle.

"Maybe Uncle knows too..."

"It's an old story."

He waved his hand.

"But more important is the dragon armor. Listen carefully. Dragon armor is made from a dragon's corpse. If you happen to defeat a dragon... "

Nasrula listened to her uncle's story. He explained every detail meticulously. When she finished listening, she had no questions left.

"I understand. With this, I should be able to make dragon armor. If there's a chance, don't hesitate to try. Got it?"

Nasrula nodded. She understood dragon armor well.

(But...)

Something still bothered Nasrula.

"Uncle?"

"Hmm, what is it?"

"Why did you teach me how to make dragon armor? I don't quite understand, but if dragon armor is valuable, shouldn't the method of making it also remain unknown—no, shouldn't it stay secret?"

"Yes..."

Ring Wearing, Weapon Equipping, Armor Putting On

85


## Page 088

"Then, why?"

"Considering what I am, that's all I can do."

The uncle put on his pipe and took a deep breath, exhaling smoke that obscured his face.

"Really, I would be the same as him. I don't want you to go adventuring either. But you're not the kind of kid who would change your mind once you've made up your mind. No matter what anyone says, if you say you're going, then you'll go."

"..."

"... Then, the only thing I can do for you is to teach you something that might help you survive."

"Uncle..."

"Come back. It doesn't matter if the adventure is successful or not. Just come back alive."

86

COMMANDS—To walk through the dungeon...


## Page 089

Here it is. This is all I can ask of you.

Nasrula hugged without saying anything. She knew that if she spoke, she would start crying.

(Auntie)

Nasrula thought while looking at the armor.

(Thanks to Auntie. I got the best armor.)

She took the armor. It was lighter than plate mail. When she tried to pierce it with a sword just now, no scratch appeared. It's clear that its defense is high.

She looked away from her previous armor. She switched the sword to Stormbringer and stepped on the descending stairs. The 25th floor underground awaited her.

To wear armor, use the W command. Pressing [W] will ask which armor you want to wear. If you're unsure which one it is, pressing [?] is a good idea. A list of armors will be displayed. After confirming, choose the armor you want to wear.

It's important to note that when wearing new armor, you need to take off the previously equipped armor first. You must remove the old armor before putting on the new one. This applies to shields, gloves, helmets, and boots as well.

Some armors cannot be worn unless a specific armor is removed first. A Hawaiian shirt cannot be worn over armor. You must take off the armor first. Also, cloaks are equipped over armor. Therefore, once you put them on, you cannot change your armor until you take off the cloak.

The command to equip weapons is w. Pressing [w] and selecting the desired weapon will smoothly proceed unless the weapon is cursed. If you're unsure which weapon to choose, pressing [?] will display a list of weapons, and you can select one by choosing an alphabet. If you don't want to carry any weapon, pressing [-] is a good idea.

Ring wearing, weapon equipping, armor donning

87


## Page 090

Finally, there is a command to equip a ring. It's the P command. Enter [P], and you can select which ring to put on. However, only one ring can be equipped on each hand. You cannot equip more than three rings. If you want to put on a new ring while already having one on each hand, you will have to remove one of them.

R T A

Remove, Take off Remove armor, Remove ring

Nasrula took off her plate mail.

It was covered in scratches. Several grooves were scratched into the chest piece, and part of the shoulder was missing. If compared to a human, it would be like a warrior who had fought to the death with numerous injuries. The scars shone like medals.

(But, I've done well to last this long...)

Nasrula stared at the armor. She had worn it since purchasing it on the 6th floor underground, and had never replaced it until reaching the 24th floor underground. She had been slashed by a zombie's sword, bitten by a jackal's fangs, and clawed by a dragon's claws. It had been a rough use. It was miraculous that its defensive power hadn't dropped even after such intense battles.

"Really a masterpiece, wasn't it?"

Nasrula stroked the armor and muttered.

"Miss, that is a masterpiece."

The shopkeeper addressed her as she stared at the armor.

"This is a special piece made by the renowned master craftsman, Sir Hyperion. Although it lacks magical power, it's unsurpassed as his final work. Such items are rare."

"Maybe so. To me, it doesn't seem all that special..."

Nasrula showed no particular interest. Indeed, the black-painted armor looked sturdy. The chest piece was thick, and the overall balance was good. It was clearly not a cheap, inferior item.

88

COMMANDS—To walk through the dungeon...


## Page 091

However, there was no denying that it was far from perfect.

Nevertheless, it was a fact that there was nothing particularly remarkable about it.

"Stop being foolish."

The shopkeeper seemed to be indignant at her indifferent tone and raised his voice.

"Stop being foolish. This armor has a soul infused into it."

"Soul?"

"Yes. It will protect you better than mere magic-infused armor. I can clearly see it."

"I can't see anything."

"That's because you're younger than me. If you could see it, I would give you the store and retire quickly. I'm in business because I can see things others cannot. I can see the soul rising from this armor."

"It's not a matter of resentment."

A cursed armor is useless. It only reduces your defense. I had no intention of buying armor that wouldn't help.

"Absolutely not."

The shopkeeper pounded on the breastplate, and a dry sound filled the shop.

"This armor is really good. You'll see if you try it out. Buy it just to see if you like it."

The shopkeeper stared at Naslura seriously.

Naslura smiled wryly and decided to buy the armor he recommended. Of course, she did not believe his claim that it had a soul infused into it. She had to buy it anyway, as it happened to be the one she liked. There was also a slight influence from his overly earnest recommendation.

"Please come back when you return."

With a new armor wrapped around her, Naslura was greeted by the shopkeeper.

"What do you mean?"

Take off the armor, take off the ring

89


## Page 092

" No, I really want to hear how it fits you. After all, I recommended this armor with confidence. If it broke right away or didn't serve its purpose at all, that would affect my credibility. "

"What if it really broke?"

"If that happens, I'll return double the payment."

"I trust you. That line."

"It's fine. So, please come back alive."

The shopkeeper's words were correct.

The armor proved more than useful. It kept her safe until she finally changed to a new one. Even if I had paid double, it might not have been enough.

It might be true that there's a soul inside.

"Thank you."

She whispered to something invisible.

90

COMMANDS—To walk through the dungeon...
SOURCE


## Page 093

I didn't want to throw it away. I wanted to carry it with me until I returned to the surface.

However, the dungeon has reached level 24. Although we defeated the Medusa, there are surely more monsters like her waiting ahead. We had no choice but to leave them behind to survive the battles.

Narsula hugged the armor tightly before slowly placing it on the ground.

The T and A commands are used to remove armor.

The T command is used to remove one piece of armor at a time. If you are wearing a single piece of armor, that piece will be removed. If you are wearing multiple pieces of armor, it will ask which piece you want to remove. Enter the alphabet corresponding to the armor you wish to take off, such as K for chain mail, B for shield, M for gauntlets, or H for helm, and it should come off unless it is cursed. If you don't know which piece of armor to remove, try entering 1 to check the armor list and then enter the corresponding alphabet to remove the armor.

The A command is used to remove all armor at once. Press 2 if none of your armor is cursed, and all armor should come off. Enter 3 to remove your weapon and become bare-handed.

To remove a ring, use the R command. If only one hand has a ring, press 4. If both hands have rings, make sure to check which one you want to remove. Unless it is cursed, the R command should easily remove the ring.

Throw

Blood splatters on the dungeon floor.

Clain panted heavily as he pulled his short sword out of the goblin's body. The dead goblin collapsed onto the floor, having lost its support.

"Ah well, I messed up this time."

Clain touched his right shoulder and felt the leather armor torn through, revealing the raw flesh underneath.


## Page 094

Warm blood was flowing out.

"Since I fell into a pit trap and Mike is worried about me, maybe I should head back quickly to heal my wound..."

Just as Klein was thinking this, a loud cry echoed through the dark cave, reminiscent of a raven's call.

With narrowed eyes, Klein discerned the enemy's true form, and couldn't help but let out a curse.

Covered in dark green scales, with emotionless amber eyes, and a jaw lined with sharp teeth, there was no doubt it was a lizardman.

Hastily switching his weapon to a bow, Klein shot an arrow at the approaching lizardman. Two of the four arrows grazed the lizardman's body, but no fatal wound was inflicted. In the meantime, the lizardman was using its sword to shield its head while gradually closing the distance between them.

Klein was overwhelmed by a sensation that his feet were giving way.

"F***!"

Throwing away his bow, Klein threw his short sword at the approaching lizardman.

The sword tore through the air, flying straight towards the lizardman's head, but was easily deflected when the lizardman thrust its sword forward again.

If he doesn't run, staying in combat is the foolish choice... What now!?

A moment's hesitation allowed the lizardman to close in. With a triumphant cry, the lizardman swung its sword and charged forward, sensing the taste of Klein's flesh. Saliva bubbled from its mouth continuously.

There must be something. Something...

Klein kept his gaze on the lizardman and reached into his sack with one hand. Various items' textures slid across his sweaty palm.

When the lizardman was just a few steps away, Klein's hand touched a cold glass bottle. His right hand moved faster than his thoughts. A potion was aimed at the lizardman.

92

COMMANDS—To walk through the dungeon...
SOURCE


## Page 095

The man's head shattered, white liquid splashing over its face.

"Guuaaaaah—!"

The lizardman let out a scream, swinging his sword in a direction completely different from where Klein was.

Dodging the lizardman's frenzied swings, Klein rushed to the hallway on the upper floor.

Behind him, there was a grumbling sound of disappointment as the lizardman let out a growl, unwilling to let its prey escape.

"Hmm, damn you, my lord."

Sighing, Klein took a step forward into the hallway.

In NetHack, when using thrown weapons, using items to throw, or feeding food to pets, use the t command.

For using bows, slings, or crossbows, first equip the weapon with the w command, then specify the projectile with the t command and indicate the direction. Of course, you can also throw arrows without equipping the bow, but the power when thrown by hand will be less than when shot with a bow.

Next, for throwing items, most items don't have much use when thrown. However, when throwing potions at monsters, if they hit, the potion

Throw

93


## Page 096

You can give the effect of a potion to monsters. For example, if it's a potion that makes you unable to see, the monster will be in a state where it cannot see the player for a while.

That said, it's not a good idea to throw potions at monsters recklessly. After all, if it's a potion that restores vitality, the monsters' wounds will also heal as a result.

Finally, regarding feeding your pet, you don't have to do it frequently. If you want to train your pet, just give it food occasionally.

k ^D

Kick 蹴る

Ping!

With a clear sound of a steel breaking, the dart needle that was inserted into the keyhole of the treasure chest flew apart.

"Ahn, mooh!"

Tike threw the dart without its tip into the corner of the room and sat down on the floor. Having tried to pick the lock like a thief, he couldn't manage it well. Using the darts he broke earlier, this is his fifth attempt.

Tike glared hatefully at the pentagonal keyhole. If there were a key that fits this keyhole, he could get the contents without such trouble, but the keys he has are triangular and square ones only.

"Why would anyone put a lock on it!!"

Michael, who had been walking around the room, turned to Tike and meowed "nya". He probably thought he was being called.

Now Tike has two choices:

He can give up on the treasure chest and leave, or continue trying to pick the lock until the key opens. Another option is to carry the chest around until he finds a pentagonal key, but that's out of the question.

94

COMMANDS—To walk through the dungeon...


## Page 097

"Alright!"

Tike decided to engage in a thorough battle.

Removing the hair ornament that had been pressing down on her fringe, she held it in her right hand. This golden hair ornament was given to her by a boy the day before entering the dungeon. She knew without trying the 6th pin that the dart couldn't open the lock. Something softer like wire would be needed.

"Sorry, Filian."

Muttering this, Tike inserted soft wire into the keyhole.

After over an hour, Tike finally gave up. The pure gold pin of the hair ornament she had picked up was hopelessly bent and could no longer serve its purpose.

"This! This! This!"

Tike shook the treasure chest with all her might. The sound of things inside rattling was annoying. Michael, who had been sleeping beside her, woke up and meowed, "Nyaa."

"...Let's go."

Tike, exhausted, stood up unsteadily. She picked up her backpack and headed towards the door at the back of the room. She had left the hair ornament by the side of the treasure chest.

When she touched the doorknob, it didn't budge.

(There's a lock here too?!)

Anger welled up in Tike's heart. Taking a step back, she took a deep breath.

"HAAAA!!"

With determination, she delivered a front kick.

With a loud noise, the door flew apart as if torn from the hinges.

Although Tike finds hymns difficult to remember, she has never been outdone in physical training.

Feeling somewhat refreshed, Tike was about to leave the room. But something caught her attention.

"Ahh!"

Tike couldn't help but shout. There was no need to open the treasure chest's lock

Kick

95


## Page 098

It would be fine if we could just kick it apart!

Tike turned around and ran back, kicking the chest with all his momentum.

At that moment.

"Kyaah!"

A thunderous sound accompanied by a pillar of fire rose from the chest, enveloping Tike's feet.

The chest had a trap set on it.

"Ach, ach, chichi-chi..."

After burning his feet, Tike managed to pick up several dozen scrolls.

Of course, they were all completely blackened and charred.

There are several ways to use the k command. You can kick monsters, structures like doors and walls, or items. In each case, the procedure is the same: input (k) and then indicate the direction with the number keys. However, when you kick something other than a monster, it is common to injure your feet, especially at low levels. When injured, you lose hit points and your dexterity decreases. It will heal naturally over time, but during this period, the weight of the items you can carry decreases, making things rather troublesome.

96

COMMANDS—To walk through the dungeon...


## Page 099

Kicking monsters deals damage to them. In particular, the "kick" of a Samurai and Priest is powerful, and they can knock down monsters in shallow layers with a single kick.

Normal doors can be opened with the o command, but to open a door that is locked, you have to use a key, credit card, or break it with a kick. However, once a door has been broken with a kick, it cannot be closed again. It would be wise to refrain from breaking a door if you plan to use it later, especially if you need a secret room. Kicking a wall will only hurt your feet, but if it's a hidden door, you can break it like a visible door.

Kicking an item usually causes it to move in the direction you kicked it. However, kicking a potion may cause it to break due to the impact, so it's best to avoid doing so. The distance an item moves depends on its weight and your strength (heavier items won't move). Also, keep in mind that kicking a treasure chest can destroy its key.

#f #1

Force, Loot Open, Examine Contents

"Enough already! Ugh!"

Tike growled as he swung his sword at the ogre in front of him. Excalibur easily split the ogre's torso, and the upper body fell back with a clean cut. Over the corpse, another monster emerged. This time, it was a demon enveloped in flames.

Tike's surroundings were filled with the corpses of monsters. He had lost count of how many there were.

"!"

Tike blocked a dragon breath attack from a distance with his shield. The Blue Dragon's "Thunder Breath" reflected off the mirror-like surface of his shield, striking several monsters.


## Page 100

While taking out the monster, it disappeared into the corner of the room.

None of the lightning, fire, or any magic had any effect on Tike. The qualities and equipment he acquired while wandering through the dungeon rendered light beams and magical attacks ineffective. And the almost invincible scale mail made from a gray dragon's scales protected Tike from most attacks.

The dragon endured several slashes but eventually fell. It didn't take much time for the other monsters to follow the same fate...

"Phew... Is this the end?"

Tike threw a treasure chest onto the floor. Chests and coffers were found one after another, and Tike, half-exhausted, gathered them all in one place.

There were about eight chests in total. Finding this many chests in one room was a first for Tike. He saw castles and armories higher up, but they didn't have chests scattered inside like this.

In front of the mountain of chests, Tike was happy. He knew from experience that the items inside the chests were usually good ones.

Tike inserted Excalibur between the lids and pressed down with his entire weight to open them. This was unusual for Tike; he usually kicks open chests. While it might be easier to use a sharp object like a sword, he hesitated to use the legendary holy sword for such a task.

"But I'm so tired..."

Thinking casually that a legendary holy sword wouldn't break or chip, Tike moved on to the next coffer. Without much time, all the lids opened.

"This... I don't need. Pass, pass, pass, pass, pass, pass!"

Tike picked up items one by one and started inspecting them. There were powerful items like Gauntlets of Power, Reflective Shield, and Regeneration Ring, but in the end, Tike chose only a few scrolls.

He already had everything else.

98

COMMANDS—For walking through the dungeon...


## Page 101

Using #f and #l two commands, you can open chests and long cabinets and take their contents. To open a chest, there is also a method of breaking it by kicking it with the k command. Additionally, you can take out the contents by first picking up the items with the pickup command and then using the a command to "use" the chest, but this method becomes inefficient as you may need to temporarily drop some of your items on the floor to pick up heavy chests.

To use the #f command, you must equip a weapon with a sharp point such as a sword, or a weapon that can be used to bash, such as a pickaxe or mace. After inputting the command, you will be asked to confirm, and if the equipped weapon is unsuitable for opening the chest, a message will appear indicating so.

To use the #l command, stand on top of the chest and input the command. First, you will be asked if you want to take the contents out, and if you answer with y, the names of the items inside will be displayed one by one, each requiring a y or n response.

After displaying all the items, you will be asked if you want to put something in the chest, and similar to taking items out, you will be asked about each item you are carrying.

Opening, viewing contents

99


## Page 102

When you open a chest, it's unlikely that you'll put something inside, but this procedure is common when using convenient tools like sacks or holding bags (especially if you put items in a holding bag, the total weight will drastically decrease! ), so it's not a waste to remember it.

Eat Eat

Nasrula was extremely hungry.

It had been a long time since she lost her last food supply. The grocery store was far away. First of all, she didn't have any money. She thoroughly searched this floor, but there were no fallen food supplies. She could barely find a water fountain, but it wouldn't fill her stomach.

Food, especially meat. Meat was what she needed.

If she kept going like this, she would faint from hunger.

"Please, anything will do. Just come out."

Holding her stomach, she saw a door in front of her as she wandered through the dungeon.

Her hopes rose. It's common for monsters to be in the room right after opening the door. She hesitated, having been attacked by monsters and sustaining serious injuries before. If she was lucky, there might be two or three. No, as long as they could satisfy her hunger, the more the better. She intended to use all kinds of magic and items to defeat the monsters.

Nasrula leaned against the door. She took a deep breath and opened the door.

The room wasn't particularly large. Instinctively, she scanned the room, but she didn't see any monsters.

For a moment, she thought her hopes had been dashed.

(No luck)

She felt the strength draining out of her body.

However, when she heard a growl from the back of the room, her expression brightened. She focused on the point in front of her, to her right, which was the farthest from her. There it was. A jackal. Its red eyes gleamed, and its sharp fangs were bared, intimidating her.

100

Commands—To walk through the dungeon...


## Page 103

The creature is large. It was the biggest jackal she had fought.

"Whoa!"

Nasrula let out a cheer.

"Protein!"

Before the jackal could attack, Nasrula lunged forward with all her might, swinging her sword. But it was deflected to the right. Due to hunger, her body lacked strength. Normally, her opponent's neck and torso would have been cleanly severed.

Before Nasrula could reposition her sword, the jackal attacked. Her sword barely blocked the jackal's teeth. The teeth and sword entangled, and the jackal's stench hit Nasrula's nose.

Nasrula retreated while swinging her sword, but it only grazed her ear.

"Fucking hell."

Nasrula continued attacking, but it wasn't going well. She was being pressed back by the jackal's claws and teeth. This wasn't a difficult opponent under normal circumstances, but now it was proving challenging. Her arm lacked the strength to swing the sword effectively.

(If I don't act now, I'll be eaten before I can eat.)

Before her strength ran out, she had to make a final counterattack. She thrust her sword forward and crouched down.

"Come on!"

As Nasrula gathered her strength, the jackal leaped. There was no intention to run away. The jackal intercepted Nasrula's attack with its teeth, halting its movement. The jackal pressed forward, but Nasrula did not yield. Without retreating, she pushed the sword forward.

Her determination to pierce the jackal's flesh was intense. Using all her remaining strength, she pushed against the much stronger jackal.

Feeling the disadvantage, the jackal retreated to increase the distance between them.

"Gotcha!"

Taking advantage of the brief opening, Nasrula swung her sword. Since the jackal had just retreated, it couldn't dodge. The fatal blow shattered the skull, and the brain matter splattered, along with the eyeball that fell out.

Eat

101


## Page 104

It was instant death.

"Phew!"

Nasrula lets her body relax.

"Meat, meat, meat, meat!"

She stares at the corpse while wiping her saliva.

The e command is a command to eat.

If you have food and are not in combat, you can eat at any time by pressing the ① key. Even without food, if you are on top of a monster's corpse, you can press the ① key to eat the monster's remains.

Eating replenishes nutrition, allowing you to continue your adventure. Additionally, by eating certain monsters, you may inherit their qualities.

COMMANDS—To walk through the dungeon...


## Page 105

The character's condition is shown on the status line at the lower right of the screen. When hungry, it becomes "hungry." If you continue without eating, it will show "weak," and your Str will drop by one, making it difficult to cast spells. If left alone further, it will progress from weak to fainting, and eventually lead to death.

When hungry, combat ability drops significantly, making it extremely disadvantageous. If you reach fainting, you won't even be able to engage in proper combat. It would be best to eat before reaching weak.

Even the strongest character cannot win against hunger. Continuing an adventure without eating monster corpses is almost impossible. Moreover, by eating monsters, you can gain advantageous qualities. Although there may be hesitation, try eating first. You might find it delicious once you get used to it. Of course, the freedom to say, "Elves never eat goblin carcasses!" still exists. Just as there is the freedom to die of hunger.

Pay

On the cloth spread on the floor, various items were arranged. This is a shop marked with a signboard reading "Deebee's Curios" located inside the dungeon.

The fact that there is such a store in the dungeon was surprising to Tike. He had always thought that the dungeon contained only monsters, traps, and other things that wanted to kill him. He had never seen a potion of an unknown color or a spellbook with gold lettered titles. There was also a coat-like garment dyed in strange colors, meant to be worn over armor.

Tike, walking restlessly among the rows of items, stopped in front of a ring. The intricately worked ring, adorned with flowers, looked like a small wreath. It was probably a magic ring imbued with some kind of power, but more than that, it seemed to be an engagement ring for a wedding ceremony.

Pay

103


## Page 106

It looks like a ring.

Tike crouched down and gently picked up the ring.

"Ma'am!"

"Yes!"

Startled by the shopkeeper's voice, Tike almost dropped the ring.

"That's 466 zmork, ma'am."

The shopkeeper, who had been polishing a shield at the end of the shop, paused his work and looked at Tike through round-rimmed glasses. The shopkeeper's rosy face seemed to be asking silently, "Would you like to purchase it?"

"Eh... and... ha..."

Tike blushed. She was embarrassed that she had reached out for the ring without knowing what it did. She didn't even know what effects it might have.

"Ah... this ring... what is it exactly?"

"Well, I'm not really interested in such things. What matters is how much it can be sold for."

As the shopkeeper resumed his work, Tike hurriedly asked.

"But if we don't know what it is, why does it have a price?"

"It's just a merchant's instinct. That ring is definitely a find. I'd stake my shop's reputation on it."

Tike sighed. In this shop, they put prices on mysterious items. It seemed that the only reliable thing was her own judgment.

After putting the ring back, Tike walked around the shop collecting food, healing potions, and wands that had proven effective so far. However, regarding spellbooks, she collected only those she had never seen before.

"This one is 260, that one is 400. And the food ration there is three for 250."

Tike arranged the gold chips as the shopkeeper listed them.

"Right, thank you very much."

104

COMMANDS—To walk through the dungeon...
SOURCE


## Page 107

If you take the money, the shopkeeper will no longer bother to look at the Tikey. Having finished stuffing his backpack and turning toward the shop door, Tikey suddenly remembered the ring.

That ring... it was just under Tikey's feet.

Tikey raised his head and glanced sideways at the shopkeeper. The shopkeeper, facing away from Tikey, was diligently polishing his shield.

Tikey compared the shopkeeper's back with the ring for a while, then kicked the ring with his toe. The round ring rolled quickly and managed to slip through the open door and out into the street.

The shopkeeper remained turned away, unaware.

(Whew!)

In his mind, Tikey cheered and was about to leave the shop when.

"Ma'am, 466."

"Ahh, well..."

Reluctantly, Tikey began to untie the money belt.

Pay

105


## Page 108

In the real world as well, you must pay the price for any item you purchase. However, the fact that there is a separate command p (pay) in NetHack can be attributed to the nature of NetHack itself.

Whether to pay the store owner is left to the player's free will. However, if you leave the store without paying, it can lead to trouble (refer to the Command Introduction section for "#w" to see what happens).

If you intend to pay, after picking up the item, input "p" and all the items' prices will be automatically paid from your gold. If you don't have enough gold, you can sell unnecessary items by dropping them using the d command, but you will only receive about half the purchase price. There are also stores that specialize in selling wands and rings, and other items cannot be bought from such stores. Most stores will buy gems, but it's worth remembering that many gems picked up in the dungeon are worthless "glass balls" with a value of 0. However, some genuine gems can be bought for very high prices, and certain uses can earn divine favor. In this sense, the archaeological gem appraisal skills of an archaeologist prove to be very useful.

Now, since ancient times, many adventurers in this world have been working on the theme of "how to deceive the store owner and obtain items for free?" Here, we will only briefly mention a few methods. They are using pets, kicking, polymorphing (changing form), and teleportation (causing someone else to teleport).

Rest 休憩する

The wound was deeper than I thought. Blood continues to gush from the Minotaur's claw marks, showing no signs of stopping. No matter how many times I change the bandages, they remain red.

(If only I had a healing potion at this moment)

Even a deep wound would heal instantly. But the scrolls and potions have already been used up.

106

Commands—To Walk Through the Dungeon...
SOURCE


## Page 109

"Then, it seems we have no choice but to wait."

Nasrula sat down. The wound was treated with herbs. After resting for a while, she might be able to move again. Ideally, she would rest in a small room with the door locked, but her injuries were too deep. If she encountered a monster, it would be the end. She had no choice but to wait.

Nasrula sighed.

(I've adventured for quite some time now)

She couldn't remember when she entered the dungeon. Was it a week ago, a month, two months? It felt like she heard her aunt's tearful protests very recently, yet it also seemed like it was a year ago that she ignored her friend's advice.

When she passed through the dungeon gate, she was filled with fear.

"There are monsters over five meters tall"

"It's said that there's a dragon at the back who kills anyone who approaches with its breath"

These rumors clouded her mind and amplified her anxiety.

However, Nasrula's desire to avenge her parents was stronger than her fear.

Her father was killed by a monster in the lower dozens of floors of the dungeon. Her mother, shocked by this news, fell ill and died shortly after. Orphaned, Nasrula was taken in by her aunt and uncle, who had no children.

Her uncle was a blacksmith who made farming tools. He was stubborn like a typical craftsman, but he was kind to Nasrula. No matter how bad his mood, he never raised a hand to her. Even when scolding her, he only raised his voice slightly and never screamed. When she cried, he always hugged her. Nasrula loved her uncle's chest, which smelled of iron.

In contrast to her gentle uncle, her aunt was much stricter. Discipline was particularly strict, and if there was even a slight lack of proper behavior, she would not hesitate to yell. She even hit Nasrula once or twice. If she neglected household chores or wanted to play, she wouldn't be allowed inside when she returned home. Usually, with her uncle's mediation, she could still get in for dinner, though she often missed it.

The only time she spent a night in the storage room was when she was a famous adventurer. 

Resting

107


## Page 110

When she visited the town where Thruul lived, she lied to her aunt and went to listen to the adventurers' stories. The stories were so enjoyable that she couldn't bring herself to leave, and by the time she returned home, it was already dark. Naslura asked her aunt to let her in, but her aunt refused to open the door at all.

"Where did you go today?"

"..."

"Of course you went to the adventurers. You know very well."

"Aunt, please listen to me."

"I have no interest in hearing the story of a daughter who won't listen to me. Spend the night outside to cool your head."

Naslura knocked on the door many times, but there was no response anymore. She went crying to the storage room. It was spring, but the mornings and evenings were still cold. Shivering, she entered the

108

COMMANDS——To walk through the dungeon...


## Page 111

She spent the night without sharing a bed.

"Be ladylike" was her aunt's catchphrase, and the education to that end was strict.

However, Nasrula did not resent her aunt's policies. Perhaps her aunt had sensed that she strongly inherited her father's blood. That was why she insisted on thorough female education. She wanted to prevent Nasrula from following in her father's footsteps and turn her into an ordinary woman. She understood the aunt's intentions all too well. When she spent the night in the storage room, a blanket and night food were properly placed there. She knew that her aunt did not dislike her.

If possible, Nasrula would have liked to live with her uncle and aunt. But she couldn't. The adventurous spirit she inherited from her father could not be contained by mundane activities.

At sixteen, Nasrula told her foster parents that she wanted to join a guild to train as an adventurer. Of course, both her uncle and aunt opposed this. They wanted her to marry and continue the family business. They repeatedly urged her to live a life of loving a husband and nurturing children as just a woman.

But Nasrula did not give up.

It might be dangerous. It might be reckless.

Still, she could not stay away.

Nasrula pushed through her foster parents' opposition and joined the guild three years ago.

"!"

The jackal's growl pulled her back to reality. Its fangs and red eyes were directed at her. It was a threat. It was about to attack at any moment.

Nasrula stood up. The time for sentimentality was over.

The command is a rest command.

By pressing the key once, time advances by one unit without taking any action. However, if injured, hit points will recover.

This may seem like an meaningless command, but the rest command is optimal for recovering stamina without the power of healing. Combined with the E command, it can restore a significant amount of hit points.

Rest

109


## Page 112

# Turn Purification

"Hey?"

Tike hesitated as he reached for the door handle of the room, feeling a strange sensation. He retracted his hand from the knob.

Through the door, a certain atmosphere seemed to be transmitted.

To put it in an analogy, it was similar to the feeling Tike had in the worship hall of the temple where he grew up. Priests generally have acute senses regarding spiritual beings. Since their purpose of training is to converse with the divine, this is only natural.

"Ah..."

Tike closed his eyes and calmed his mind, trying to sense the surroundings delicately.
(Oh, this is wrong)

This sensation is not from a higher spiritual being. It feels somewhat murky. Thinking that there might be a "sanctuary" on the other side of the door, it turned out to be something unwelcome. Tike gripped his mace in his right hand and repositioned his shield in his left.

He pushed the door open forcefully from the shoulder.

"Uwah!"

The room was filled with undeads of various colors. There were purple hues that had begun to rot, pink skin peeling off. There were greens crawling with maggots, and brownish-gray like the bandages of a mummy.

The undeads that noticed Tike were slowly approaching with unsteady steps. While each one individually would be manageable, being confronted by such a group went beyond just being creepy; it made him feel nauseous.

Tike could not suppress the rapid decline of his fighting spirit. Even though he knew it was hopeless, dealing with this kind of opponent was a girl's instinctive aversion that she couldn't control.

He was at his limit.

In just a few seconds, he would likely break down and run away screaming.

110 COMMANDS——To walk through the dungeon...


## Page 113

"Sh, guardian god Crom… please help me!"

Without conscious thought, Tike muttered the name of the deity as her outstretched finger drew a symbol in the air.

The zombie at the front of the line was enveloped in a blinding light.

As the light faded after a few seconds, the zombie collapsed and stopped moving, like a puppet whose strings had been cut.

"Crom!"

With renewed momentum, Tike shouted the name of the deity again.

The mummy, dragging its decayed bandages, was enveloped in a white glow...

But the mummy did not fall. As soon as the light faded, it resumed walking as if nothing had happened.

"Stop it why! ——Crom!"

She hurried to shout again, but the result was the same.

The light shattered instantly, and the mummy's steps did not stop.

Tike held back the urge to cry and readied her mace. Her will, which had almost faltered once, was now holding steady. In the end, survival

Purification

111


## Page 114

In order to rely on nothing but one's own strength.

"Chrom's fool!"

Tike shouted as he charged at the Mummy.

Tike would eventually realize that his inexperience was causing the Undead's turn to fail, but that is another story.

Turn Undead is a special skill possessed by Priests and Knights. There is a spell with the same name, but its effect is the same, and it can destroy one Undead body. However, while the spell has a limited number of uses, the two aforementioned classes possess this ability innately and can use it unlimited times. Note that there is also a wand called Undead Turning, but this merely instills fear in the Undead and causes them to flee, and its effects differ from those of the skill and spell.

The effect of Turn extends to visible Undead within sight. If you are in a room, all Undead within the room are targets, but if you are in a corridor where you can see only one step ahead, only the adjacent Undead are targets. Additionally, Undead whose location is known through telepathy are not affected even though they are not actually seen. The same applies if you are blind.

Now, whether Turn will successfully destroy the Undead depends on the character level and the monster level. Against Undead that are a few levels lower than yours, Turn is almost guaranteed to succeed. For higher-level Undead, they may resist (regain) the Turn, and the success rate decreases as the level difference increases.

However, considering that no experience is gained from a successful Turn, and that only one Undead can be destroyed per Turn, and that Turn is reliably successful only against Undead that are several levels lower, attacking with your weapon might be more advantageous. Furthermore, blessed weapons hit Undead more easily and deal greater damage. If you have a blessed weapon, you should attack without hesitation.

112

COMMANDS—Walking through the dungeon...


## Page 115

Detect Trap, Untrap

"Damn it, thieves' tricks don't suit me at all!"

Yoshitane's scream echoed uselessly through the dungeon.

On the 12th floor, Yoshitane had found a long coffin.

It wasn't unusual. Sometimes there could be three or four coffins or treasure chests. The lock on this long coffin required a square key, but he didn't have even one key. As usual, he tried to kick it open, but this time he felt something. He sensed hostility—perhaps something akin to murderous intent—from the long coffin.

This ability was what allowed him to survive as an adventurer. Yoshitane well knew that he couldn't ignore this feeling—yet he wasn't a thief.

Yoshitane had received basic training from the guild. But that was just training. He passed the exams. However, his instructor whispered to him, "Don't think you'll actually find a trap and try to disarm it."

He's clumsy, to put it simply.

No, perhaps the term 'clumsy' doesn't fit Yoshitane. He was quite dexterous. It's just that disarming traps wasn't suited to his nature.

For nearly two hours, Yoshitane sat in front of the long coffin, trying to determine the type of trap that might be set.

"...I can't figure it out! I can't figure it out!"

Yoshitane lay flat on the floor, face down. He definitely understood that a trap must be set. In fact, the fact that it took two hours to realize this merely proved that his sense was correct.

Disregarding the trap and kicking it open was also an option. The trap would surely activate, but the contents inside could still be obtained. However, if the trap released flames, it was one thing. But if it contained sleep gas or paralyzing poison needles, it was another matter to consider.

Detect Trap, Untrap

113


## Page 116

It was left to him. There was even a possibility that he might be devoured by goblins or orcs while asleep.

Yoshitne's mind was filled with numerous possibilities, all of which were discarded into the corner of his mind like trash.

He knew the easiest choice remained. Although it was annoying to have to make this decision after spending so much time, there were no other options left, so there was nothing he could do about it.

"Are you giving up?"

Sighing and slumping, Yoshitne stood up unsteadily. Behind the long coffin, Urshi also noticed the movement and stood up with a yawn, saying "Well, well."

While obtaining a fine sword and armor was important, Yoshitne also understood that surviving was the most crucial thing. He was just ashamed of himself for wasting two hours without making a decision.

After falling victim to a teleport trap, Yoshitne found himself in front of this long coffin again.

114

COMMANDS——To walk through the dungeon...


## Page 117

It will happen every time. Whether he knows that there is nothing inside when he successfully disarms the trap is another matter.

Sometimes, traps are found on doors or the lock parts of chests. Most traps set on doors explode when you try to open them. Traps set on chests or treasure boxes can contain poison needles or sleep gas, among other types.

The command to discover these traps is #u. After inputting this command, you need to indicate the direction to investigate the trap. If you find a trap, you will be asked whether you want to disarm it. Entering (y) here will start the process of disarming the trap, but if you fail, you will trigger the trap instead.

Disarming traps requires a certain degree of dexterity, so be careful. If your Dx value is around II, you should know the importance of 'knowing one's limits.' Sometimes, triggering such a trap can be fatal, so be cautious. As expected, once a trap is triggered, there won't be any more traps to find.

Also, traps set on the floor or elsewhere may be discovered using commands like s. These traps indicated by □ cannot be disarmed. However, you can determine the type of trap using the □ command.

Sometimes, it is necessary to intentionally fall for a trap. For example, if you find a teleport trap in a sealed-off dungeon, you would probably jump into it regardless. Even if it is a trap, thinking flexibly can lead to unexpected uses.

Trap Detection, Trap Disarming

115


## Page 118

Engrave write

"Ugh, there's nothing here, isn't it"

Standing in the center of the dimly lit room, Tike let out a disgruntled voice.

Having descended the stairs to this floor, this is the third room he has come to, but there is absolutely nothing here. No items have fallen, no treasure chests are present.

Until now, every room he had checked was dark, so time was wasted just confirming that "nothing" was there. If a monster had appeared, Tike wouldn't have been as upset. Most monsters can be eaten after being defeated.

"Still, it's nice to have a peaceful moment like this sometimes"

Tike muttered to himself, letting down his backpack from his shoulder. Having walked around quite a bit, he had been feeling hungry for some time. From the jumbled contents of his pack, Tike took out a K ration packet. He had picked up one recently and saved it, looking forward to tasting it.

Tike also thinks that the food situation in the dungeon is not bad at all. However, that's without considering the taste.

"Oh, no"

Tike realized he had left the door open. Previously, he had once failed to notice a monster approaching while engrossed in eating. With the rusted hinge, Tike forced it shut and looked down at the words written on the floor. They were carved with a sword or something, in strong male handwriting: "It's not a good idea to slash at the Acid Blob." The name must be "Yoshitane," as his signature is readable.

"Mr. Yoshitane... A strange name"

116

COMMANDS—To walk through the dungeon...
SOURCE


## Page 119

Tike chuckled and searched to see if there were any other writings. It didn't take much time, and he found several similar ones. Tike forgot about eating as he read each one.

"Altars can distinguish between curses and blessings."

"If you fall into a trap, remember its location. Traps are effective against monsters as well. ——Nasrula"

"If you're hungry, steal from shops. You'll get more cream pie than you can eat. ——Clein"

Tike read the words with sparkling eyes. These people who wrote them must have been thrown into unknown dungeons like Tike, learning one way to survive at a time. Tike felt that the loneliness deep within him was slightly healed.

"Well, what should I write next? ♡"

Holding a magic marker, Tike fell into thought. There was so much to write. The fact that Tike had survived until now was never due to luck or chance.

Write

117


## Page 120

Aku, and Tike's stomach growled.

He tore the silver paper off the ration that he had been holding and bit into the semi-solid object.

"What is this!"

It's bad.

It's thin and tasteless. Tike had never eaten anything this bad before. Since coming to the dungeon, it seems.

Tike peeled off the lid of the marker and wrote vigorously on the floor.
{Do not eat K ration unless it is a life-or-death situation. ——Tike}

The E command is a somewhat special command. As an action, it simply involves writing characters on the floor, and there is no problem with that. However, one must wonder what use it can be. The written characters have no meaning if no one reads them. In version 98 of NetHack, it is a single-player game, and the dungeon is rebuilt every time you create a new character.

However, there may exist random messages generated on the dungeon floor. These could be useful advice or perhaps lies that seem true. It is up to you to judge their truthfulness.

The characters written on the floor will wear away over time and eventually become illegible, and finally disappear. The time until they become illegible or disappear varies depending on how they were written. There are two methods: writing on the accumulated dust with your fingers or a wand, or engraving them into the stone floor with a sharp weapon like a sword. Writing on the dust is easy, but the characters will become illegible after passing over them a few times. Engraving into the stone will last several times longer, but there is a risk that the weapon used will deteriorate. Regardless of which method is used, passing over the characters will shorten their lifespan.

According to unverified information, it seems that by engraving the name of a monster's god and standing on it, almost all monsters' attacks can be sealed.

118 COMMANDS——To walk through the dungeon...


## Page 121

Call, Naming 名付ける

"Chit chit chit"

Yoshitane whistled while waving the orc meat in front of him. The stray dog in front growled, following Yoshitane's hand with its eyes.

Yoshitane had lost his beloved cat Fommy in a fierce battle with several Urks-hai he encountered a few floors up. When Fommy was bisected by an Urk-hai's curved sword, it felt as if a part of his body had been torn away.

At that time, he thought he would never again explore the dungeon with a partner. He did not want to experience such sorrow and pain again.

However, now that the sorrow of losing Fommy had faded, he realized how much Fommy's existence meant to him.

In this harsh and dark dungeon, Fommy was the only friend Yoshitane had. They fought together, searched for food, and cautiously approached each other. Sometimes, Yoshitane would distract the shopkeeper, and Fommy would steal something from the shopfront.

In any case, Fommy was irreplaceable.

"There's no one to take his place."

Whenever Yoshitane thought about Fommy, he muttered to himself. However, even without a replacement, a new partner was needed. Someone who could fill the void in his heart.

It was at such a time that Yoshitane met a stray dog. Perhaps, having been abandoned by other adventurers, it had become semi-wild in the dungeon. The dog's unusually lustrous black fur spoke of its wild nature.

The moment their eyes met, Yoshitane felt that this dog could be a partner. He couldn't put his finger on why, but it was the same feeling he experienced when he first met Fommy.

Name

119


## Page 122

I pulled out the oak's flesh from my backpack and waved it in front of me. Although it growled, it was clear that it was paying attention to the meat.

Yotsune lightly threw the meat. The black dog hesitated slightly, but unable to resist hunger, it took the meat into its mouth.

"See? Is it good?"

Without paying any attention to Yotsune's voice, the black dog continued eating. It seemed to be ignoring his existence entirely.

Shrugging his shoulders, Yotsune left the room. Since he couldn't tame it, keeping it around might become dangerous. However, he didn't have the intention to kill this black dog. So, he had no choice but to let it go.

As he reached out to Nob and opened the door,

several arrows flew from the darkness of the corridor. Most were deflected by his crystal plate mail, but one grazed his temple.

"Damn, what's this? Poisoned arrow...?"

The image of the poison arrows used by oaks flashed through Yotsune's mind, but in the darkness, the silhouette of a monster began to appear. A half-human, half-horse form...

"A centaur! Why would a centaur be in Yendor's dungeon?!"

Centaurs are a race that originally live in grasslands and mountains. Even if the dungeon of Yendor is vast, they wouldn't normally reside within it.

That moment of hesitation resulted in a powerful kick from the centaur to Yotsune's torso.

All the air was expelled from his lungs, making it impossible to breathe. His vision blurred, and his consciousness drifted away.

In the corner of his vision, he saw the centaur's hooves. However, he couldn't even draw his katana.

"Until now!"

In some part of his consciousness, Yotsune shouted.

Just then, he saw the black dog biting at the centaur's shoulder.


## Page 123

Yoshitane shook himself to clear his mind and drew his katana, making a single slash.

Spray of the centaur's red blood danced in the air.

"Ha ha. …Thanks."

Yoshitane smiled wryly and thanked the black dog. When he stroked its head, it wagged its tail happily in response.

"You've got a name too, don't you? Well, let's see…"

Yoshitane looked at the black dog. The lustrous fur color reminded him of something from his father's hometown.

"Alright, from now on you're Urshi. How does that sound, Urshi?"

"Baou!"

The black dog—Urshi barked once and followed Yoshitane.

Naming

121


## Page 124

Commands——To walk through the dungeon...

The C and #n commands are both commands to give unique names to items or monsters. The C command allows you to give unique names to monsters.

Like Yoshitsune, you could name new pets, or give liked names to monsters you encountered (without fighting them) during your adventure.

The #n command is used to give special names to items such as weapons. This method can be useful for easy differentiation when you have multiple identical items. Some kinds of "named blades" can be obtained by this method, though the details are unclear.

---

Dip ——浸す

"I'm going to the spring, Mike"

Klein sighed and spoke to his beloved cat Mike.

Mike didn't seem very interested and just gave Klein a quick glance before starting to groom himself enthusiastically with his forked tongue. At Mike's feet were scattered bones of a recently eaten dwarf.

"Hmph, when my stomach swells up like this..."

With a look of exasperation, Klein approached the spring near the end of the small room in the dungeon. The dark blue spring occasionally made small bubbling sounds.

Klein looked at the sword in his right hand.

This was the cause of the gloominess that usually brightened Klein's disposition. It was a sword he had picked up while walking on the upper level of the dungeon, but he had equipped it without thoroughly examining it, which was a mistake. The sword was cursed with a malevolent curse. No matter how much he tried to discard it, the sword clung to his hand as if it were part of his right hand.

"I don't have any scrolls to remove the curse... What should I do?"

As he muttered to himself, a memory of Alvena's words suddenly came to mind.

"Klein, I'll teach you something good when you go down to the dungeon tomorrow."

---

COMMANDS——To walk through the dungeon...


## Page 125

Albena, who had won a lot of money in a drinking contest against a giant man, was in high spirits as she began to speak.

"Continuing exploration in the dungeon is difficult, but the curses on items are quite troublesome. The quickest way to remove them is by reading a scroll of解除, but there are other methods as well."

"Hmm, what are those methods?"

While glancing sideways at a drunk Barbarian being led away by two people, Klein asked.

"You can try immersing the item in a spring in the dungeon. If you're lucky, the curse will be lifted."

"What if you're unlucky?"

"There are times when that happens."

Saying this, Albena lowered the front of her dress, revealing three crooked claw marks running from her right shoulder down to her collarbone.

"These are wounds inflicted by a Water Demon's talons."

As she traced the wound on her chest with her fingers, a thin smile appeared on Albena's lips.
Naah—Go.

Hearing the familiar sound, Klein turned around, and Mike was right behind him.

"Alright, wait here. You never know what will come out."

Mike called out to Klein, who slowly and cautiously immersed his sword in the spring. As the blade sank into the water, something emerged from the bottom of the spring.

What came out of the water was a beautiful woman. Her naked body, reminiscent of a pale maiden, constantly dripped with water droplets, and her hair, reaching her feet, emitted a blue phosphorescence.

(Yikes! A Water Nymph!)

Shouting inwardly, Klein tried to run away hastily. But his limbs wouldn't move. He was entranced by the nymph's beauty, and his body wouldn't obey. Even Mike, who hated humans, was rubbing his cheek against the nymph's feet.

After a while, when Klein regained his senses, the nymph was no longer there.

Immerse

123


## Page 126

"Damnit, got me good"

Upon checking my inventory, as expected, several items were missing. Even my only armor, leather armor, had been stolen.

But at that moment, Klein noticed his right hand felt lighter. Following this, a laugh escaped Klein's mouth.

"Y-Yeah, this is a good experience too..."

Klein directed his gaze to his right palm.

It seems the nymph has also stolen the cursed sword of trouble.

The #d command to soak objects has two uses: soaking items in potions and soaking them in springs.

Soaking items in potions isn't particularly useful. Especially mixing potions together usually results in most of them evaporating or turning into water. However, there are some useful applications; holy water can bless an item just by being soaked, and poisons can be applied to arrows and such to create powerful poison arrows.

124

COMMANDS—To walk through the dungeon...


## Page 127

When items are immersed in a spring, various effects can occur. There may be cases where monsters appear, or where one receives curses or blessings. Indeed, it can vary greatly. When a player's character is at a low level, it might be quite a rash act to attach an item to a spring simply to receive a blessing. It would be wise not to do so unless absolutely necessary or in a desperate situation. Furthermore, according to rumors, there is a possibility of obtaining the legendary holy sword Excalibur by immersing a certain sword in a spring.

↑

Teleport (ティレポート)

Yoshitsune's consciousness was dominated by a vague feeling for some time.

"...I feel awful."

His condition was so off that he repeated this several times within just a dozen steps down the corridor. It wasn't that something was wrong with his body or that he felt pain anywhere; however, he couldn't deny that he felt off.

"Maybe it was that can of food... I didn't check what was inside before eating the cans in the long casket recently."

Since Yoshitsune hadn't killed any eatable monsters lately, he had eaten the cans in the long casket without properly checking their contents.

From then on, he began to experience a sensation of mild fever. His limbs were controlled by a floating sensation, and his head was hazy as if covered in mist.

"It didn't seem like poison—"

He thought to himself. At that moment, Yoshitsune was hit by the sensation of his body floating. It was a different sensation from dizziness. Something seemed to be rising from within his body, and his body was being pulled towards it...

In the next instant, Yoshitsune realized that the surroundings were completely different. Instead of the corridor he had been walking in just now, he had arrived at some large hall. Moreover, he could see several Killer Bees in front of him.

"N-no Teleport trap!?"

Teleport

125


## Page 128

In an instant, though Yoshitane was surprised, he was also a newly minted warrior. In the next moment, he drew his katana and with a seppuku strike, split the killer bee's torso in two.

"Next!"

As he swung his katana to cut down a bee beside the one he had just dispatched, the familiar sensation struck him again.

"?"

In the next moment, Yoshitane found himself surrounded by thousands of gold coins.

"Here... this is... the Croesus vault as I've heard about it?"

There were rumors that several vaults were hidden within Yendor's dungeon. It was said that Croesus, a wealthy citizen of the town, had built these vaults in the dungeon to keep most of his wealth safe from theft. Yoshitane was right in the middle of one of them. He managed to stuff some of them into his backpack, but there were far too many to fit.

"Haha, there's always something. But what kind of evil deeds would one have to commit to end up here,"

---

COMMANDS—For walking through the dungeon...
SOURCE
>>>


## Page 129

"Where does all the money come from?"

Yoshitane chatted lightly, but he soon realized that he couldn't say such things. There was no door-like object in the narrow vault room; only heaps of gold coins existed, groaning loudly.

Yoshitane diligently searched for a hidden door, but all the walls appeared to be just walls. Even after half an hour had passed, no door showed up.

"Are you kidding me! How am I supposed to stay locked up here!"

Shouting this, Yoshitane pounded the wall hard. Pain shot through his fist, but he didn't care and continued pounding. He would rather be killed by a monster than die trapped in such a small room.

And then, at that moment, the wall opened, and a man's face appeared.

"Huh? A face I don't recognize, who are you!"

The moment Yoshitane raised his head, the man raised his voice.

"I am Yoshitane the Samurai..."

"Yoshitane? Never heard of you. Who gave you permission to enter this vault? Throw all the gold coins on the floor and follow me. Then I'll take you out."

There was nothing Yoshitane could object to. While he did have some gold coins, compared to rotting away in such a place, they were certainly worth less.

However, as he reached for his wallet in his backpack, Yoshitane noticed the familiar sensation rising from within his body.

Before him was a Kiwi's head, and from somewhere, a roar echoed.

"Thief! I have teleportation ability!"

While slashing at the Kiwi with his sword, Yoshitane listened to the voice.

It seems that the can contained meat of a monster with teleportation ability, and that ability had transferred to Yoshitane.

Teleportation

127


## Page 130

"Such a power beyond my control! I wanted to shout, but I restrained myself. I remembered the rumor that the guardman Coloesas was looking for is a robust warrior."

Beings that can teleport can eat them or acquire teleportation ability by taking a certain ring. To teleport, press the Ctrl key while typing 't'. However, just having the teleportation ability alone does not allow you to teleport to your desired location. The ability to control teleportation must be obtained through another method. Also, skilled mages can learn to control teleportation.

However, there are times when you cannot control your own will to teleport, and at other times, teleportation ability activates suddenly without your desire. If teleportation occurs suddenly while shopping, it would be a tragedy (or a comedy).

But, if you use teleportation instead of fleeing during combat to escape, or to save movement points, you can freely run around the dungeon. This advantage is hard to give up.

Although this teleportation ability is very convenient, it has one major weakness. Teleportation consumes a lot of stamina. Even if you are full, you may become hungry after teleporting a few times. Please be careful about this point.

# s

Sit - 座る

The dungeon was filled with a stench reminiscent of rusted iron blood.

Standing among the piled corpses of goblins and oaks, Klein panted heavily. Klein's armor was drenched in deep red from the splattered blood.

"Strange room, Mike"

128

Commands - For walking through the dungeon...
SOURCE
>>>


## Page 131

Clain called out to Mike without looking at him. Mike paid Clain no mind and continued to feast on his stomach.

"Such a room filled with goblins and orcs is rare. Maybe there's some great treasure here."

Smiling slyly, Clain approached the long chest he had kept an eye on during the battle.

The long chest was equipped with a sturdy lock.

"Hmph. It seems I can manage this."

Clain muttered to himself as he examined the lock from various angles. He took a lock pick from his sack and carefully inserted it into the keyhole.

After some trouble, Clain's nimble fingers slowly turned the lock pick to the right, and a faint click was heard.

Peering into the chest, Clain let out a disappointed sound.

Having checked if there was a trap, he opened the chest, but found only one familiar vial of poison potion inside.

"Fucking hell! All that trouble just for this one?"

After stuffing the potion back into his sack, Clain sat down on the dungeon floor.

The coldness of the rock felt good.

Suddenly, Clain noticed that Mike was nowhere to be seen. Looking around, he saw something moving in the corner of his vision. It was to the right, and close by.

What was moving was a hobgoblin.

The body of the hobgoblin, which was lying down with its back against something, was slightly trembling.

(Indeed, I must have knocked it out...)

As Clain repositioned his sword, the hobgoblin's shadow revealed their only friend in the dungeon.

"You did this, Mike."

Mike didn't even look at Clain and continued to eat the hobgoblin. With sharper fangs, Mike struck the hobgoblin's arm, and then shook its head from side to side. The dead hobgoblin fell to the ground, and Mike sat on its back.

129


## Page 132

The object that had been concealed revealed itself.

It was a finely crafted throne.

The throne was adorned with intricate workmanship, its elegant curves suggesting it might have been crafted by a master dwarf. Klein considered it might be a new trap he had never encountered before, and carefully examined the throne to see if anything was set.

"Nothing here. Boring."

As he muttered to himself more and more as he explored the magic palace, Klein abruptly sat down on the throne with vigor.

"…!"

As Klein took a breath, a voice echoed through the dungeon.

"Hm. So you said something about 'summoning' or whatever..."

Before Klein could continue, his mouth suddenly closed.

A thick black fog filled the vast space of the dungeon.

The spreading darkness moved like living beings, coalescing into the images of reviled monsters.

When the darkness finally dissipated, the room was filled with countless monsters, too numerous to count in an instant.

COMMANDS—To walk through the dungeon...


## Page 133

And, filled with their beastly cries.

"Phew, troublesome. Now even the undead troll won't do."

Standing up, Clay pulled out his still blood-stained sword.

"Alright then... let's go, Mike!"

With a loud cry, Clay ran towards the group of monsters.

As for Mike, he was still leisurely enjoying his meal as usual.

When playing NetHack, if you want to sit on the throne, use the #s command.

It might not happen immediately after sitting down, but after repeating it several times, various effects will appear. These effects are not always favorable for the adventurer; sometimes they can lead to disasters. For example, sometimes monsters may appear, and at other times, all your gold may vanish.

Nevertheless, there is still value in trying to sit on the throne. This is because the Wish (wish) effect allows you to obtain the most desirable items for an adventurer.

If you find a throne, it's best to prepare for the worst case scenario before sitting down. Unfortunately, the throne disappears after sitting on it a few times, so you cannot remain seated indefinitely.

Jump ジャンプ

Mike looked at his master, Clay, with a puzzled expression.

Clay was jumping around Mike's body like a flea, happily.

"M-Mike. This is good. Oh, t-t-t"

Clay nearly bumped into Mike and quickly stopped.

Fhgya!

Mike let out a painful cry as Clay stepped on his long tail.

"I'm sorry, I'm sorry"

Jump


## Page 134

Mike gives a resentful cry to the repentant Klein.

"Are you saying sorry? Anyway, this Klein is interesting. With these jumping boots, it seems I could move faster than you."

Shaking his head at Klein's satisfied expression, Mike moved to a corner of the room. It seemed he had made a wise judgment to stay away from his fidgety master for now.

As Mike approached the door, he turned around. Klein was still hopping around excitedly in the jumping boots. Mike looked around for something nearby that might be fun to play with, but found nothing more than a rotting jackal corpse.

At that moment, Mike caught a whiff of a beast-like odor while scanning his surroundings.

Just as Mike turned to look, a huge foot came down in front of him.

Gyaar!

Fortunately, Mike dodged quickly, but his recently stepped-on tail was stepped on again, causing him to scream in pain.

"What's wrong, Mike?"

Looking at Mike, Klein saw him running towards him desperately.

Behind Klein was a large shadow.

"Oh, Ohgga!"

Seeing the approaching Ohgga, Klein took a step back.

Suddenly, the ground beneath Klein's feet crumbled. Klein's body fell into a deep pit.

Painfully, Klein looked up to see Mike peering down at him from the edge of the pit.

"F***. A trap at a time like this... wait, if I use this..."

As the sound of Ohgga's footsteps grew closer, Klein concentrated all his strength in his legs and pushed off the ground. Floating in mid-air, Klein's body leaped over the pit and landed in front of Mike. The loud thud echoed through the dungeon.

---

COMMANDS—To walk through the dungeon...
---


## Page 135

```
Phew, that was close.

"Phew, that was close"

Clein breathes heavily as he looks at the trap.

A goblin had fallen into the trap, its sharp fangs bared and it let out a roar of anger.

"Well then, Mike, I'll set some bait for you now."

Mike responds with a pleased chirp.

Clein switches his weapon to an arrow and shoots a poisoned arrow at the goblin.

If you can jump, you can use the #jump command to make your character jump.

By jumping, you will be able to easily escape from monsters and also be able to escape from certain traps. However, if you are wearing Jumping Boots and have too many items, the weight might prevent you from jumping, so be careful.

Jump

133
```


## Page 136

# Monster's Ability

Vibrations shake the dungeon as if the ground itself is trembling.

A red dragon, wrapped in dark crimson scales, walks through Yendor's dungeon.

Strangely, behind the dragon was the form of Mike. Grown to the size of a leopard, Mike walked obediently behind the dragon with supple steps.

"Mike..."

A voice emerged from between the dragon's sharp fangs.

Though the voice was oddly hoarse due to the difference in vocal organs, it was unmistakably Clain's voice.

"I heard there was a ring that could turn one into a monster... This must be it."

Clain looked at the golden and silver rings on his sharp claws.

In the dim light, two rings with strange magical power glimmered.

Huff!

Suddenly, Mike let out a warning growl like when he threatens an enemy.

Clain lowered his long neck to look ahead, and saw a monster. A monster.

On the giant humanoid body of the monster, an ugly bull's head grew. Its twisted horns, below which the monster's deep red eyes stared intently at Clain, were visible.

(Minotaur!)

Clain thought to himself.

The Minotaur charged at Clain. A thick bundle of strong flesh writhed under its copper-colored skin.

(Usually I would run away... But not now!)

Opening the mouth with fangs interlocked, a crimson flame burst from Clain's mouth towards the Minotaur.

For a moment, the surroundings were filled with intense light.

134

COMMANDS—To walk through the dungeon...
SOURCE


## Page 137

Through his thin, slanted almond-shaped eyes, which were narrowed to slits, the Minotaur charged forward fearlessly, despite half of its left side being blackened by flames. Despite this, there was no sign that the Minotaur was slowing down.

Clain stopped the attack with his breath of fire and tried to bite the Minotaur with sharp fangs. To protect his head, Clain extended his left arm, and the Minotaur's fangs dug into it. As Clain shook his head from side to side, the left arm was torn off at the shoulder socket with a loud crack.

Seeing the Minotaur spilling fresh blood, Clain felt certain of victory. However, at that moment, a sudden pain shot through his left chest. Upon inspection, he saw that the Minotaur's right arm had struck him, piercing through his tough scales and deeply embedding itself in his left chest.

"Guuaaaaah—!"

The dragon's pained roar shook the air.

The Minotaur continued to bury its right arm deep into Clain's chest and attempted to crush his massive heart.


## Page 138

As consciousness faded, a sudden change occurred in Klein's body, having prepared to face death. The outline of the dragon's body became blurred, and his massive limbs gradually shrunk.

"Hey?"

Noticing this, Klein found himself back in his familiar form. He checked his left chest, but there was no sign of injury.

Looking up, he saw the Minotaur looking around. It seemed to be searching for where the dragon that they had been fighting had gone.

Suddenly, the Minotaur looked down and spotted Klein. After a moment of silence, it roared, its fangs emerging from the burned mouth.

"M-Mike... Run!"

With that, Klein ran off with Mike.

If you are tired of exploring the dungeon as a human character, you might enjoy playing as one of the monsters that live in the dungeon.

The easiest way is to wear both the Ring of Polymorph and the Ring of Teleportation. While the effects won't appear immediately, after some time, the game will ask what monster you want to transform into, and all you need to do is input the name of your desired monster.

At this point, if the transformed monster has special abilities, you can use the #m command to activate those abilities.

For example, if you transform into a Red Dragon, pressing the #m command allows you to attack with fire. If you turn into a Werewolf, you can summon your pack of wolves.

In any case, once you have transformed into a monster, you should use the #m command to check its special abilities. This will make your NetHack experience much more enjoyable.

136

COMMANDS—To walk through the dungeon...


## Page 139

Wipe Face

"What the hell is going on!"

Clain was running through the dungeon.

His and Mike's bodies were covered in large amounts of white cream and torn pie crust.

Reaching the door of the room, as he tried to open it, the lock was already secured. Quickly pulling out a lockpick, Clain began to pick the lock.

From behind the door that Clain had entered, strange men in odd clothing started running out. The moment they spotted Clain, they began throwing cream pies at him. One of the pies hit Clain's face directly as he turned around.

"Ugh"

Clain wiped the cream that stuck to his face with his right hand. Mike vigorously shook his head from side to side, trying to knock off the pie.

(Maybe it was a mistake to bring those?)

As Clain opened the door, he muttered.

---This bizarre escape began with an incident at a certain store.

"Welcome, Clain! You always come to Tom's scroll shop."

When Clain, exploring the dungeon, opened the usual door leading to the room, he was greeted by a cheerful voice.

Standing in front of the surprised Clain was an elderly man who appeared to be quite old and short. From the hem of the black robe wrapped around his body, his wrinkled face and emaciated arms resembling withered branches could be seen.

Behind the elderly man, who wore a static smile, there were countless scrolls carelessly laid out on the ground. Clain cautiously stepped into the store and picked up one of the scrolls near his feet. The elderly man immediately told Clain the price of the scroll he had picked up.

"It's expensive. What kind of scroll is this?"

Clain unfolded the scroll and began muttering words that made no sense as he traced them.


## Page 140

He stopped.

"Ah, no. That..."

With the old man's panicked voice, the scenery around him began to blur. A few moments later, Klein teleported to another place.

"Phew. Glad I tied the reins to Mike."

Mike blinked his eyes and looked around.

Biiii -- Biiii --.

An alarm suddenly rang out in the dungeon.

"What is that sound?"

Clain muttered, frowning at the noise.

In the dark room, the sound of a door opening was heard somewhere.

And then... the first cream pie hit the side profile of the stunned Clain.

(If this keeps up, I'll turn into a human cream pie.)

Now, Clain's body was covered with cream pies without any gaps, looking as if he were made entirely of cream pies.


## Page 141

He was presenting a demeanor similar to that of a mummy.

Behind Klein and Mike, as expected, were those strange-clad individuals who were chasing them. As Klein, cornered, opened door after door, a small shadow suddenly blocked Klein's path.

"Are you going to pay up, then? Or do you want to eat more cream pie?"

It was the owner of the scroll shop, wearing a black robe. The smile of good humor had vanished from the old man's face, and what came out of his mouth was a dry, cold voice.

It seemed that Klein had somehow returned to the scroll shop while running around.

Behind the old man were men holding cream pies and rubber hoses, waiting for Klein's reply.

"Alright, alright."

Sighing, Klein paid the owner for the scrolls.

After Klein handed over the money, the men's figures disappeared instantly, leaving the old man behind.

"What was that... I wonder..."

Klein whispered weakly. The owner of the scroll shop began calculating the money.

Mike, next to Klein, was licking the cream off his face, looking pleased.

To wipe your face, use the #w command.

Usually, using the #w command will just remove dirt from your face, but if your vision is obscured by something like a cream pie, it can help you escape from a blind (blind) state.

While this #w command may not be used very often, it's not a bad idea to remember it in case you find yourself in any situation within the dungeon. 

Wipe your face

139


## Page 142

# Rub

The central hub of the thief guild, a notorious city of vice called Bals.

In this city, one street corner, Zaldos Street, had become almost a lawless district due to its poor law and order. There was a tavern called The Golden Horn there.

On his way back from training at the guild, Klein opened the door of the tavern to have a drink before going to his quarters. To his surprise, it was unusually crowded that day. He squeezed into an available seat and started drinking some bad-tasting ale when a new customer sat down next to him.

"Kek kek. What a rare guest you are."

The mage turned rogue, Groth, who was also the owner of the tavern, said in a vulgar voice. As he laughed, his fat body shook up and down.

Setting aside the full mug of ale, Klein glanced over and saw a woman taking off her travel cloak made of leather. Her beautiful golden hair flowed down from under the hood.

"Long time no see, Groth."

The woman greeted Groth.

"That's right. Well, let's have a drink then."

Groth poured some ale into a silver glass he rarely used. After gulping down the amber-colored liquid, she wiped her wet lips with her left hand and smiled.

Groth and the woman continued talking for a while, but when a new customer came in, Groth went to take his order with reluctance. She took the heavy wine jug in her right hand and began pouring her second drink.

While Klein was admiring the woman, a loud noise came from a table near the entrance of the tavern. Turning around, Klein saw a wooden chair flying towards them. It was headed towards the woman next to him. Instantly, Klein stretched out his left arm and caught the chair mid-air.

Relieved, Klein looked in the direction the chair had come from and saw two people. 

140

COMMANDS—For walking through the dungeon...


## Page 143

They were facing off with weapons. One was Reglos, a regular customer known as the Drunk Priest. The other was Layla, a Walhalla warrior with a refined northern appearance.

"Even if you are a woman, those who insult my god shall not be forgiven!" Reglos raised his voice, slightly nasal from the alcohol.

"Here we go again. It always happens when he's drunk."

Clein muttered to himself.

"Hey Clain. Regy has been a childhood friend since we were kids, try to help him out. The opponent is Walhalla warrior Layla."

Clain gave Groth a worried look as he hurried back.

"Help him out, huh. When he gets drunk... "

While they were talking, Reglos and Layla's swords clashed twice or thrice, sending sparks flying. The customers gathered around Reglos and Layla didn't try to stop them; instead, they started betting on which one would win. They were shouting encouragement or insults to the person they had placed their bets on.

"Groth, use this."

The woman threw an old lantern at Groth.

"Oh, a magic lamp!"

"In return, I'll clear all your debts."

Groth grinned and nodded, rubbing the lamp in his hand. Dark gray smoke began rising from the lamp. The smoke spread and formed the shape of a large man.

"...At your service, my lord."

A deep voice echoed from the large man's mouth.

"Jin, throw out the two causing a commotion over there."

"As you wish."

Jin casually approached Reglos and Layla, grabbed both by the collars with his thick arms, and tossed them through the open door without any trouble. 

"Thanks for that."

The woman poured some drink into Clain's cup.

"What's your name? I'm Clain."

rubbing


## Page 144

"Albena... they are calling her that"

Clain and Albena raised their glasses and drank them dry at the same time.

If you find a lamp while exploring the dungeon, you should check if it lights up using the 'a' command. If a dark room becomes bright, it's just a normal lamp. However, in most cases, if nothing happens, it is likely a magic lamp.

If you luckily obtain a magic lamp, it would be good to try rubbing it with the '#' r command. In most cases, a genie will appear after rubbing it a few times.

However, keep in mind that the effects of a magic lamp can vary depending on whether it is blessed or cursed.

# v

Version

The version of NetHack you are currently playing can be known by using the #v command.

142

COMMANDS—To Walk Through the Dungeon...


## Page 145

@

Pickup ON/OFF

While playing NetHack, if you press the @ key, you can pick up items simply by walking over them in the dungeon. (This is the Pickup ON state.)

And if you press the @ key again, it switches to Pickup OFF, and you will no longer be able to pick up items unless you press the □ key. In other words, the Pickup state alternates between ON and OFF every time you press the @ key.

While the Pickup ON state may be convenient, there are items that can bring disaster just by picking them up, so it is not recommended for beginners.

$

Gold

The $ command allows you to know the amount of money you currently have. However, since the amount is displayed on the screen during play, you rarely need to use the $ command.

¥

List of Identified Items

By entering ¥, you can see a list of all the items you have discovered so far. This is different from the i command in that you can see items that you have used, read, or discarded. By looking at this list, you might be able to guess what items still have unknown details. It is therefore recommended to use it occasionally.

Other Symbols

143


## Page 146

Amulets 魔除け

Welcome to Weyrdian's Decorative Items Shop. Here you will find amulets. However, we do not deal in the Amulet of Yendor that some customers seek so desperately. That amulet is one that only Lord Yendor possesses deep within the dungeon... Other amulets are available here, so please feel free to browse.

amulet of change

Change Amulet

The moment this amulet is worn, the sex of the wearer is reversed. It has no other effects.

amulet of esp

ESP Amulet

This amulet grants the ability of telepathy. You may be able to sense the power of this amulet when using a blindfold.

amulet of life saving

Life Saving Amulet

If your hit points drop to zero and you die, you can be revived if you are wearing this amulet. However, there are cases where you cannot be saved.

amulet of reflection

Reflection Amulet

This amulet reflects the power of light-based spells and staves. In a way, it might be considered the most valuable amulet.

144

ITEMS—Dungeons Await Your Tools
SOURCE


## Page 147

Amulet of Restful Sleep

Amulet of Restful Sleep

This amulet does not show its effects immediately upon wearing. However, after a long period of time, it suddenly induces sleep in the wearer.

Amulet of Strangulation

Amulet of Strangulation

Wearing this amulet causes something to stick to the throat and attempt to stop the wearer's breathing. In most cases, it is cursed and can be fatal.

Amulet Versus Poison

Amulet Against Poison

When worn, this amulet grants resistance to poison. Even if stung by a bee or pierced by a scorpion's sting, one can remain in perfect health.

Amulet of Yendor

Amulet of Yendor

Not only does this amulet confer no benefit on the wearer, but merely possessing it prevents floor-to-floor teleportation and increases the energy required to cast spells. It can only be obtained at the deepest level of Yendor's magic dungeon. Also, there are said to be fake Amulets of Yendor.

Armors 防具

Oh? Ah, welcome. This is Maxis's armor shop. Look, we have plenty of helmets and armors in stock. Of course, some of them might be cursed. But there are also blessed ones and those enchanted with magic. I don't really understand much about magic, but I know about the forms of armors.

Armors—防具

145


## Page 148

Here's the translation:

Check out the catalog here and compare it with our items. If you can find a balance between your budget and requirements, you should be able to find the best item.

ARMORS Armor

Armor worn on the body. While many armors include helms and gauntlets, we don't treat them as such, so please forgive us.

leather armor

Leather Armor AC-2

Made from leather hardened by tanning animal hides, this is what is commonly known as leather armor. It has the advantages of being quiet and very light, but it is not reliable for defense. However, it does not corrode or rust.

orcish ring mail

Orcish Ring Mail AC-2

A crude ring mail that orcs prefer to use.

ring mail

Ring Mail AC-3

An armor made by connecting metal rings. While it is relatively light for its metal composition, there is nothing particularly notable about its defensive capabilities.

studded leather armor

Studded Leather Armor AC-3

A leather armor reinforced with iron nails. While its defensive power has slightly improved due to this, it remains fundamentally a leather armor.

scale mail

Scale Mail AC-4

A leather armor with scale-like metal plates attached. It is somewhat heavy, but as a warrior, you should at least equip this level of armor.

chain mail

Chain Mail AC-5

A garment-like armor made by weaving chains and covering down to mid-thigh. This is what is commonly known as a chainmail. It makes a considerable noise when moving. Additionally, while it can prevent cuts from swords and similar weapons, it cannot absorb the impact itself.

146

ITEMS—Dungeons waiting for you with their tools


## Page 149

LEATHER ARMOR

CHAIN MAIL

SCALE MAIL

Armors—防具

147


## Page 150

orcish chain mail

Orcish Chain Mail AC-5

Chain mail used by orc warriors. As expected of warriors, it has been well maintained, and it does not fall short compared to regular chain mail.

elven mithril-coat

Elven Mithril Coat AC-5

Chain mail made by elves. Crafted from magical metal called mithril, it weighs as much as leather armor but offers the same level of defense and is also resistant to acid and rust.

dwarvish mithril-coat

Dwarvish Mithril Coat AC-6

Chain mail made by dwarven craftsmen. Like the elven mithril coat, it is very light and has improved defense. It is likely due to the fact that it was crafted by dwarves, who are born warriors.

splint mail

Splint Mail AC-6

Chain mail with small plates of metal tightly fitted over the chain links. While its defense is higher than regular chain mail, its weight is also greater. It still gives a sense of being somewhat in between chain mail and plate mail.

banded mail

Banded Mail AC-6

Chain mail made by stacking several bands of metal plates. It is quite heavy, but its defense is considerable. Wearing this level of armor should provide some peace of mind in Yendor's dungeon.

bronze plate mail

Bronze Plate Mail AC-6

Plate mail made from bronze. While slightly less in terms of defense due to the material, it is more resistant to corrosion.

crystal plate mail

Crystal Plate Mail AC-7

Plate mail made from crystal, crafted using a method known only to a guild on a western island. Like the bronze plate mail, it is durable and offers the same level of defense as regular plate mail.

plate mail

Plate Mail AC-7

Full plate mail made from one piece of sheet metal, covering almost the entire body.


## Page 151

PLATE MAIL

DRAGON SCALE MAIL

Armors—Defensive Equipment

149


## Page 152

The dragon scale mail is equipped with chain mail to ensure freedom of movement. It can be said to be the strongest armor made of ordinary materials. However, it is quite heavy and very expensive, making it difficult to obtain even from an armorer.

dragon scale mail

dragon scale mail AC-9

It seems to be a rare armor made from dragon scales. Of course, its high defense is invaluable, but what is most appreciated is that it is lightweight.

Furthermore, there may be compatibility issues, as this armor is said to be made from the scales of only one type of dragon. And, depending on the color of the dragon's scales used to form the armor, it is rumored to have various special effects.

CLOAKS Mantle

A mantle worn over armor. Even if the armor is made of a material that corrodes, as long as you cover it with a mantle, it will be quite safe. In that sense, it might be a very important piece of equipment.

cloak of displacement

cloak of displacement AC-1

This mantle has the power to bend light. The wearer of this mantle will likely see their illusory image appear slightly away from their actual position. Monsters also tend to attack the illusory image first.

cloak of invisibility

cloak of invisibility AC-1

The wearer of this mantle will likely notice that their appearance becomes invisible. Yes, this mantle seals the spell of transparency. However, its defensive power is not to be expected.

cloak of magic resistance

cloak of magic resistance AC-1

This mantle has the power to defend against magic. It renders many spells ineffective for mages. You will understand how effective this mantle is when you enter the lower levels of the dungeon.

150

ITEMS—What awaits you in the dungeon


## Page 153

cloak of protection

Cloak of Protection AC-3

A much more defensive cloak than a regular mantle. It boasts armor-like defense, but it's best not to forget that it is still a cloak.

dwarvish cloak

Dwarvish Cloak AC-0

A cloak worn by dwarves, known for their excellent color sense. It may be slightly too small for humans or elves, so its defensive power doesn't fully manifest.

elven cloak

Elven Cloak AC-1

An elven-made cloak. Its magic to absorb sound allows you to move silently (without waking sleeping monsters).

mummy wrapping

Mummy Wrapping AC-0

The bandages left behind after defeating a mummy. There are rumors that if a person wearing this bandage dies, they will turn into a mummy.

orcish cloak

Orcish Cloak AC-0

A black cloak worn by orc leaders. It is purely for show and offers no defensive power.

HELMs——兜

Armor that protects your most important part—the head. It might also have various magical effects on your head.

dwarvish iron helm

Dwarvish Iron Helm AC-2

A helmet that dwarves prefer to wear. It boasts good defensive power but is somewhat heavy.

Armors——防具

151


## Page 154

Elven Leather Helm

Elven Leather Helm AC-1

A helmet made of leather. Intricate designs are carved all over it.

Fedora

Fedora AC-1

A brimmed leather hat. While its defensive power is not great, its major advantages are its resistance to acid and rust, as well as its lightness.

Helmet

Helmet AC-1

A plain helmet. It might be said that its lack of distinctive features is its most notable feature.

Helm of Brilliance

Helm of Brilliance AC-1

Once this helmet is worn, one can understand how it makes the wearer's mind more acute. Specifically, it is a helmet that increases the intelligence and wisdom of the equipped.

152

ITEMS—Dungeons awaiting you


## Page 155

helm of opposite alignment

Helmet of Opposite Alignment AC-1

A helmet that dramatically changes your character's attributes. In most cases, it is cursed, so the attribute change will persist until it is removed by a blessed removal spell. Even if you can remove the helmet, the attribute will revert to its original state.

helm of telepathy

Helmet of Telepathy AC-1

Wearing this helmet grants you the ability of telepathy. It might be easier to understand the power of this helmet when using a blindfold.

orcish helm

Orcish Helmet AC-1

A helmet commonly used by orcs and goblins. Although quite heavy, it provides a minimum level of defense.

SHIELDS Shields

Shields are more of an auxiliary piece of equipment. They are more useful in melee combat rather than one-on-one battles. Still, if you don't have a two-handed weapon, it might be better to use a shield.

dwarvish roundshield

Dwarfish Round Shield AC-2

A medium-sized round shield favored by dwarves. It can be considered a fairly ordinary shield.

elven shield

Elven Shield AC-2

An elven-made shield. It is somewhat light and has a decent amount of defensive power. The use of mithril silver likely contributes to its partial strength.

large shield

Large Shield AC-2

A large shield. It is about twice the size and weight of a small shield, and its defensive power is also doubled.

Armors—Armor

153


## Page 156

orcish shield

Orcish Shield AC-1

A crude shield that even the lowly orc soldiers carry. Not only is it crude, but it also weighs quite a bit, so it's preferable to use another shield if possible.

shield of reflection

Shield of Reflection AC-2

A medium-sized round shield, but what sets it apart is that the center has been polished into a mirror. This mirror reflects many light-based attacks and renders line-of-sight attacks无效的翻译结果，让我尝试重新生成：
orcish shield

Orcish Shield AC-1

A crude shield that even the lowly orc soldiers carry. Not only is it crude, but it also weighs quite a bit, so it's preferable to use another shield if possible.

shield of reflection

Shield of Reflection AC-2

A medium-sized round shield, but what sets it apart is that the center has been polished into a mirror. This mirror reflects many light-based attacks and renders line-of-sight attacks ineffective.

small shield

Small Shield AC-1

A small shield. It is the lightest among normal shields, but it doesn't offer much in terms of defense.

Uruk-hai shield

Uruk-hai Shield AC-1

A whiteish shield primarily used by Uruk-hai. Despite being an advanced breed, orcs are still orcs, and their shields are of rather poor quality.

LARGE SHIELD

SHIELD OF REFLECTION

154

ITEMS—Dungeons await you with these tools


## Page 157

BOOTS ブーツ

Boots are footwear that protect your feet... of course. But in this dungeon, there are also vicious insects that bite and won't let go of your feet. I think they are essential. There are even magical boots that can make your feet move faster or make your footsteps disappear.

Elven Boots
AC-1

These are elven boots made by elves. Like the elven cloak, they have magic that absorbs sound, allowing you to move without making any noise at all.

Fumble Boots
AC-1

At first glance, they look like ordinary boots. However, these boots contain terrible magic. The wearer will start to stumble and fall frequently. And in most cases, the fumble boots are cursed, making it a great burden to move around in the dungeon.

High Boots
AC-2

These are leather boots reaching up to the knees. They are quite heavy, but they provide defense commensurate with their weight.

Iron Shoes
AC-2

These are iron shoes. While dwarves are said to prefer them, they are quite heavy. Despite their weight, they do offer considerable protection.

Jumping Boots
AC-1

These boots greatly increase jumping power. You should be able to jump over pits and ditches.

Levitation Boots
AC-1

These are boots for levitation. However, if you wear these boots, you will no longer be able to pick up items that are lying on the ground.

Low Boots
AC-1

These are boots reaching just above the ankles. Compared to the sandals commonly used by adventurers, they are

Armors——Armor

155


## Page 158

While they are speed boots, the effects as armor are not particularly promising.

speed boots

AC-1

When you equip these boots, you will notice that your movements have become faster. In terms of specific effects, both the number of attacks and movement points increase.

HIGH BOOTS

IRON SHOES

GAUNTLETS OF POWER

HAWAIIAN SHIRT

LEATHER GLOVES

156

ITEMS—Magic awaits you in the dungeon.


## Page 159

Water Walking Boots

AC-1

When these boots are equipped, magic embedded in the soles allows you to walk on water. You can safely cross moats, which will be useful in certain areas.

Gauntlets

Gauntlets are things to wear on your hands. Some seem to have magic that seals hand-related spells, but I'm a novice when it comes to magic, so I don't really understand them.

Gauntlets of Dexterity

Gauntlets of Dexterity AC-1

These gauntlets contain magic that increases dexterity. The moment these are worn, the wearer becomes boastful of their highest dexterity.

Gauntlets of Fumbling

Gauntlets of Fumbling AC-1

Equipping these gauntlets makes you more likely to drop weapons. They could be fatal in combat. Also, they are often cursed, so wearing them even once might lead to a tragic situation.

Gauntlets of Power

Gauntlets of Power AC-1

These gauntlets increase strength. It's said that you can wield giant or ogre-like strength, and deal significant damage to enemies even with bare hands.

Leather Gloves

Leather Gloves AC-1

Leather gloves. Ordinary gloves, nothing special.

Armors—Armor

157


## Page 160

OTHERS Other Armor

For now, it's just the Hawaiian shirt that can be worn under armor. It seems useless yet useful somehow. Just don't show it to any other shopkeepers besides me.

Hawaiian shirt
AC-0

The Hawaiian shirt, Aloha (or anything else come to mind?). The only piece of armor that can be worn underneath another. If enchanted, it should prove quite useful. However, there's a weakness in wearing it visibly as it might attract the attention of the shopkeepers.

Foods Foods

Welcome, come in. This is Fortilia's grocery store. See, all sorts of things to satisfy your appetite. From candy to lamb stew.

Getting tired of eating only the monsters' corpses? Maybe you should eat some food for humans too? And if you can eat the monsters' remains, I'll even buy them from you. So, what would you like to eat? I can get anything for you.

Apple
Rinго. Nutritional value isn't high.

Banana
Banana. While popular for energy replenishment during physical activity on the surface, its nutritional value in the dungeon is only slightly higher than that of an apple.

158

ITEMS—Armor and Tools Awaiting You in the Dungeon


## Page 161

Candy bar

Candy. Has a high nutritional value for its size, like a block of sugar.

Carrot

Carrot. Contains a lot of vitamin A and is very good for the eyes. Nutritional value is low.

Clove of garlic

Garlic. Some kinds of monsters strongly dislike the smell of garlic. Therefore, they will not approach those who carry it.

Cram ration

Portable food. Slightly lighter than usual food, with slightly lower nutritional value. It can also be considered a valuable item in Yendor's dungeon.

C-ration

Military portable food.

Cream pie

Cream pie. Nutritional value is average, but it should be used by throwing at enemies rather than eating.

Egg

Egg. Sometimes rotten eggs can be found, and eating them can be fatal. Since the nutritional value is not high, you might as well ignore it. Or you could give it to your pet (though it might break if thrown).

Foods—Food

159


## Page 162

food ration

A regular food. It has high nutritional value, but it is very heavy and cannot be carried in large quantities, which is its weakness.

fortune cookie

Fortune cookie. Originally, it is a cookie that comes out in Chinese cuisine, containing a piece of paper with fortune written on it. Here, it mostly contains a little advice for the dungeon (it is not guaranteed that what is written inside is true).

K-ration

Military rations. Carried by soldiers like Sergeant and Captain. It is famous for its hard-to-describe subtle taste, and is occasionally released from the military.

lembas wafer

Lembas. A portable food of elves, and one wafer of this thin cookie-like substance provides the same nutritional value as a full meal. It is very light and can be considered the ideal food. However, it does not provide a feeling of fullness.

lump of royal jelly

Killer bee's royal jelly. The royal jelly made in the hive of killer bees has special power and is said to increase the strength of the eater.

melon

Melon. While it has the highest nutritional value among fruits, the nutritional value of fruits in general is not particularly high.

160

ITEMS—The tools waiting for you in the dungeon


## Page 163

Orange

Orange. It has nutritional value comparable to that of a banana.

Pancake

Pancake. It has decent nutritional value, but it doesn't have any notable features.

Pear

Pear. Among many fruits, it is recognized as having the lowest nutritional value.

Slime Mold

Slime mold. In NETHACK.CNF, if something is described after "fruit:", it refers to that fruit. Given its great fondness, it can be considered to have some nutritional value, including a placebo effect.

Tin

Canned goods. There are various types of canned goods, and their nutritional value varies depending on what's inside. Occasionally, you might find a can of spinach, which should prove very useful to adventurers.

Tripe Ration

Dog food. To be honest, it's not something humans should eat. You might consider eating it if you're extremely hungry, but you'll likely regret it.

Potions — Water potions

Welcome, welcome. You've come to Wendy's Elixir Shop.

We deal in potions here. From strong drinks that only dwarves can drink to fruit juices. What would you like? Want to move faster? Float in the air while adventuring? We even have potions that increase your strength or charisma. Blindness potions and confusion potions can also serve as weapons. As long as you have gold coins, you can buy anything. By the way, potions that are cursed or blessed may have different effects, so be careful.

Or, shall we buy the potion you found during your adventure? Of course, we'll pay a high price for it.


## Page 164

Potion of blindness

Potion that causes blindness

It causes blindness. If thrown at an enemy, it can significantly reduce the enemy's attack power.

Potion of booze

Alcoholic Beverage

Extremely high alcohol content, very strong drink. Most will become drunk instantly, causing temporary confusion in their mind.

Potion of confusion

Potion of Confusion

A potion that causes confusion. If thrown at an enemy, it can cause the enemy to become confused. However, as with most potions, if thrown too close, one might inhale the smoke from the potion, resulting in oneself becoming affected by the confusion.

Potion of enlightenment

Potion of Self-Insight

Upon drinking, you immediately gain knowledge of your own attributes. For example, you can discern transparent objects or teleport... and so on, making clear what attributes you possess.

Potion of extra healing

Potion of Full Healing

Restores hit points to maximum. It also seems to cure blindness (blind) and sickness (sick). Furthermore, if your hit points are already at maximum, it increases the upper limit of your hit points.

162

ITEMS—Dungeons Await These Tools for You


## Page 165

Fruit juice

Fruit juice

A small amount can distract hunger, but it's best to avoid simply writing down your favorite fruit (unless you want to drink something like "BBQ juice").

Potion of gain ability

Ability Increase Potion

When you drink this potion, one of the six ability scores will increase at random. It does not seem that strength will increase beyond 18.

Potion of gain energy

Energy Increase Potion

It raises the magic power (Pw) of the drinker. The increase is proportional to the original magic power.

Potion of gain level

Level Increase Potion

Experience level increases by 1. However, the maximum level is 30, so no further increase is possible.

Potion of hallucination

Hallucinogen

All items and monsters in the dungeon will appear as various different things. Naturally, even cute pets may look like terrifying monsters. Be careful not to accidentally kill them.

Potion of healing

Healing Potion

Some hit points are restored, and blindness caused by any reason is cured. Additionally, when hit points reach the highest, the upper limit slightly increases.

Potion of invisibility

Invisibility Potion

You can become invisible. However, how long you can stay invisible is unknown.

Potion of levitation

Levitation Potion

You can float in the air. You can avoid most traps and defend against certain monster attacks. However, you cannot pick up items on the ground anymore.

Potions——Water Potions

163


## Page 166

Potion of monster detection

Monster Detection Potion

By drinking this potion, you can immediately know the position of monsters on the same floor. Of course, since monsters move around, they may not be in the same place.

Potion of object detection

Object Detection Potion

By drinking this potion, you can immediately know the position and type of items on the same floor. There is also a possibility that monsters will pick them up first.

Potion of paralysis

Paralysis Potion

By drinking this potion, your body will instantly become paralyzed. It is unknown when you will recover. You can also use this potion as a weapon.

Potion of restore ability

Restore Ability Potion

It restores lost ability points for some reason. In most cases, it will restore strength lost due to poison.

Potion of see invisible

Invisible See Potion

You can see transparent creatures or creatures made transparent by magic. It seems that blindness will also be cured as a side effect. It tastes like fruit juice.

Potion of sickness

Toxic Potion

Some ability values decrease, and you take damage to your hit points. You may also fall ill. However, if you are plagued by hallucinogens, a shock may cause the hallucinations to subside.

164

ITEMS—Dungeons Await These Tools for You


## Page 167

Potion of speed

Speed Increase Potion

This potion doubles the movement speed of the one who drinks it. Naturally, the distance moved and the number of attacks also double. Additionally, it can heal injured feet for some reason (kicking a wall, stepping on a land mine, etc.).

Water (clear potion)

Water

Water is classified into three types. First, ordinary water. This provides a slight effect to cure hunger. Next, cursed water. Immersing any item in this will curse it, but if the character's attribute is chaotic, drinking it will restore a few hit points. Lastly, holy water. This damages demons, undead creatures, or those with a chaotic attribute. Furthermore, immersing a cursed item in holy water can remove the curse.

Rings —— Finger Rings

Welcome to the Ring Jewelry Shop.

We have a wide variety of magical rings to satisfy your needs. What kind of ring would you like? The Alluring Ring will greatly enhance your charm. The Ring of Strife will become more and more necessary as you delve deeper into the dungeon. Of course, we also have catalogs that clearly explain the effects of each ring, which you may freely read.

One thing you should be careful about is that actual effective magical rings use the wearer's energy directly. Therefore, wearing a magical ring results in high energy consumption... in other words, your hunger will increase more rapidly. If you don't have food, it's better to take them off as much as possible. 

Rings —— Finger Rings

165


## Page 168

Ring of Adornment

Ring of attraction

When this ring is worn, the wearer's charm increases immediately.

Ring of Aggravate Monster

Ring of Anger

While wearing this ring, more monsters will target the wearer.

Ring of Cold Resistance

Ring of Cold Resistance

Wearing this ring grants resistance to cold. It allows the wearer to withstand freezing rays from magic or staves, as well as ice breath from dragons.

Ring of Conflict

Ring of Discord

When wearing this ring and there are two or more monsters present, the monsters will begin fighting each other. Additionally, any pets owned by the wearer will start fighting regardless of who the opponent is.

Ring of Fire Resistance

Ring of Fire Resistance

This is a magical ring that grants fire resistance to the wearer. It protects the wearer from fire-based attacks such as spells or scrolls of fire. Even hellfire would not harm the wearer.

Ring of Gain Strength

Strength Ring

When this ring is worn, strength increases. The wearer can carry more items and deal greater damage to enemies.

Ring of Hunger

Hunger Ring

The moment this ring is worn, an overwhelming hunger sets in. The speed at which the wearer becomes hungry doubles. Other effects are nonexistent. In most cases, it is cursed and difficult to remove.

Ring of Increase Damage

Weapon Sharpening Ring

When this ring is worn, the wearer can hit the enemy's weak points accurately, increasing the damage dealt per blow.

Ring of Invisibility

Invisibility Ring

This ring has the effect of making the wearer transparent. By becoming transparent, it becomes easier to approach creatures like leprechauns and nymphs.

166

ITEMS—Dungeons awaiting you
SOURCE


## Page 169

Ring of Levitation

Ring of Levitation

When this ring is worn, you can levitate. It allows you to avoid most traps, but you will no longer be able to pick up items that fall on the ground.

Ring of Poison Resistance

Ring of Poison Resistance

A ring that grants resistance to poison. While it prevents sickness from eating rotten food, you can still remain healthy even if you eat a corpse with poison, such as a kobold.

Ring of Polymorph

Ring of Polymorph

Wearing this ring causes random polymorphs without any warning. Since the type of monster you transform into is random, there is a great risk involved.

Ring of Polymorph Control

Ring of Polymorph Control

If this ring is worn during polymorph, you can control the transformation. Transforming into powerful monsters like a red dragon or minotaur might not be a bad idea.

Ring of Protection

Ring of Protection

A ring that increases your defense. Even the best ones can provide defense comparable to chain mail.

Ring of Protection from Shape-Changers

Ring of Protection from Shape-Changers

A ring that prevents shape-change disease caused by attacks from various parasitic creatures.

Ring of Regeneration

Ring of Regeneration

A ring that regenerates one hit point per step taken. However, your hunger increases tremendously each time you regenerate.

Rings——指輪

167


## Page 170

Ring of searching

Ring of Searching

A ring that makes it easier to discover hidden doors and traps. Just by walking around, you can find these things.

Ring of see invisible

Ring of See Invisibility

Allows you to see monsters that are magically invisible or have invisibility as a quality.

Ring of shock resistance

Ring of Shock Resistance

A ring that protects you from lightning-based magic and electrical traps.

Ring of stealth

Ring of Stealth

This ring allows you to enter a room with sleeping monsters without waking them up. It's a ring that enables stealthy actions.

Ring of teleport control

Ring of Teleport Control

A ring that lets you choose where to teleport to when you do. It seems you can also choose to teleport between floors.

Ring of teleportation

Ring of Teleportation

Suddenly teleports you to a random location without any warning. Without teleport control ability, you cannot choose your destination.

Ring of warning

Ring of Warning

Wearing this ring causes it to emit various colors as a warning when a monster approaches nearby.

168

ITEMS—Dungeons awaiting you
SOURCE


## Page 171

Scrolls——Scrolls

This is Coldulyn's scroll shop. Don't underestimate scrolls. Scrolls can make or break your adventure. Identification scrolls and anti-curse scrolls are among the most important items in Yendor's dungeon. Charging scrolls can revive broken staves or lamps, and attack amplification and defense amplification scrolls can enhance the power of weapons and armor. Got it? You should understand how important scrolls are. So, which scroll do you want? Think carefully before you choose.

Oh, I forgot to mention. Once you read a scroll, it disappears. Because the magic sealed within the scroll is consumed. But as long as you know this much, you shouldn't go wrong.

Scroll of amnesia

Forgetfulness Scroll

The forgetfulness scroll can be fatal for a magician. As soon as you read this scroll, you will forget almost all of your maps and many of the spells you memorized. In a situation where you rely heavily on magic and have no high attack capability with weapons, this could be the worst-case scenario.

Scroll of blank paper

Blank Scroll

It is just plain parchment, nothing more. However, if you have a Magic Marker (magic maker), you can write on this scroll to create your desired scroll.

Scroll of charging

Charging Scroll

This scroll increases the number of uses for items like wands or Magic Markers that have limited uses. However, remember that it can only be used once for a Wand of Wish.

Scroll of confuse monster

Confusion Scroll

When you read this scroll, your hand will glow red. This red light has the property of confusing monsters. Monsters encountered immediately after reading the scroll will be confused.

Scrolls——Scrolls

169


## Page 172

A scroll that can summon monsters

Scroll of create monster

You can summon several desired monsters. However, the summoned monsters will not obey the summoner. You might also consider summoning them as food when you are hungry. Additionally, you can try to recover hit points by summoning monsters with healing powers.

A scroll that can destroy armor

Scroll of destroy armor

When you read this scroll while wearing some kind of armor, the armor will be destroyed. Whether the armor is magical, blessed, or cursed does not matter.

A scroll that can enchant armor

Scroll of enchant armor

This scroll has the power to make armor or gloves more durable. When you read it, if the armor turns silver, it indicates an increase in its defensive power. However, you must be careful if the scroll itself is cursed, as reading it will curse the armor itself.

Also, there is a risk that the armor may collapse due to excessive enhancement of its defensive power.

A scroll that can enchant weapons

Scroll of enchant weapon

When you read this scroll, the weapon in your hand will glow blue. This light increases the weapon's power and improves accuracy. However, if the scroll is cursed, it not only dulls the weapon but also seals the curse within the weapon.

Furthermore, there have been reports that the weapon may collapse if you attempt to enhance its attack power too much.

170

ITEMS—Dungeons await you with these tools


## Page 173

Scroll of fire

Scroll of Fire

This scroll spews flames from its surface as it is read. Naturally, these flames will harm and burn the reader, taking away basic hit points. However, at the same time, they can damage surrounding monsters, so if you have fire resistance, you might be able to use it as a weapon.

Scroll of food detection

Scroll of Food Detection

After reading this scroll, the location of all food on the level you are on becomes clear. It could be useful when you are hungry.

Scroll of genocide

Scroll of Genocide

When this scroll is read, you are asked to call out the name of a monster. Then, you can sweep that monster from Yendor's dungeon. However, if the scroll was cursed, you may find yourself surrounded by the very monster you tried to kill.

Scroll of gold detection

Scroll of Gold Detection

This scroll tells you the location of all gold coins on the level you are on. It will be valuable at the beginning of your adventure.

Scroll of identify

Scroll of Identify

There is no disagreement that this scroll is one of the most important scrolls among all scrolls. It reveals the true nature of any item. Whether it is the effect of a red potion or the power hidden in a staff adorned with gems, reading this scroll will bring everything into the light.

Scroll of light

Scroll of Light

A scroll that produces magical light. However, if the scroll is cursed, it may instead cover you in magical darkness.

Scroll of magic mapping

Scroll of Magic Mapping

A scroll that allows the level you are on to be mapped in your mind through magic. If there are fountains or altars in the dungeon, you can know about them as well.

Scrolls——卷物

171


## Page 174

Scroll of punishment

Punishment Scroll

This scroll contains the divine incantations. Therefore, reading this scroll will bring punishment upon you. Your ankles will be chained, and a heavy iron ball will be hung at the end of the chain. There is no way to escape this punishment except by removing the curse.

Scroll of remove curse

Remove Curse Scroll

This scroll can remove all kinds of curses that have befallen you due to angering the gods, reading a curse scroll, casting a curse spell, or equipping a cursed weapon. It promises to lift all such curses.

Scroll of scare monster

Protection Scroll

When you stand on this scroll placed on the ground, monsters will cease to attack under the name of Elbereth. Furthermore, if you read aloud the runes written on this scroll, monsters will flee under the name of Elbereth.

Scroll of taming

Tame Scroll

Reading this scroll causes the monsters near the reader to become docile. Additionally, it has the effect of calming an angry shopkeeper, likely because something was stolen.

Scroll of teleportation

Teleportation Scroll

The reader of this scroll can transcend space and move to another location. However, whether they will arrive at their desired destination is never certain.

172

ITEMS—Dungeons await you with these tools


## Page 175

Spellbooks 魔導書

Hello, welcome to Laas Louek's rare book shop. Ah, we deal with spellbooks here. The catalog is available, but I can't guarantee the contents of the books themselves. Why not? Well, I can't read Runes. But I can guarantee that all the books here are spellbooks. You can tell they're spellbooks just by looking at them, even if you can't read their contents.

So, which one are you planning to buy? What? Want to see the catalog? Fine, here it is. This is the catalog of spellbooks. It also includes a brief description of the spells. They are supposedly classified by earth-based mages.

Spellbook of cancellation

Power Drain Magic Level 7

This spell has the power to nullify magic power. When used on oneself, it can remove curses from items, but blessings and weapons sharpened by magic will become ordinary. Additionally, it can strip magical effects from living beings (such as leprechauns' teleportation ability).

Spellbook of cause fear

Cause Fear Magic Level 3

A spell that induces panic in monsters. Monsters affected by this spell will try to flee from the caster as quickly as possible.

Spellbook of charm monster

Charm Magic Level 3

This spell charms monsters and tames them. No matter how fierce the monster may be, it will start behaving like the caster's friend as soon as the spell takes effect.

Spellbook of clairvoyance

Clairvoyance Magic Level 3

When this spell is cast, the character can see the terrain within a certain distance around them. Even outside a room or down a passage, they can see the presence of monsters.

Spellbook of cone of cold

Cone of Cold Magic Level 5

A freezing ray emanates from the caster's fingertips. It is effective against ice-type spells.

Spellbook——Magic Book

173


## Page 176

There are many items, but since some dislike ice, it's advisable to choose the user carefully.

Spellbook of confuse monster

Confuse Monster
Magic Level 2

When this spell is used on a monster, the monster will become confused. It's uncertain what actions they will take, but it's certain that the possibility of being attacked decreases.

Spellbook of create familiar

Summon Familiar
Magic Level 6

This spell summons a familiar (pet). Unlike create monster, it can be treated like a pet and will not attack you.

Spellbook of create monster

Summon Monster
Magic Level 2

When this spell is cast, a monster appears next to the caster. However, the likelihood of the monster being friendly towards the caster is very low. Instead, it's worth noting that most monsters can be eaten once defeated.

Spellbook of cure blindness

Cure Blindness
Magic Level 2

Whether caused by drinking a potion or enemy magic, this spell can be recited to recover when blinded.

Spellbook of cure sickness

Cure Disease
Magic Level 3

Diseases from eating rotten food can sometimes be fatal. In such cases, reciting this spell is beneficial as it causes the disease to disappear quickly from your body.

174

ITEMS—Tools Awaiting You in the Dungeon


## Page 177

Spellbook of detect food

Food Detect Magic Level 2

Displays all food items on the level containing the caster. It will be very useful when you are hungry.

Spellbook of detect monsters

Monster Detect Magic Level 1

Displays the positions of all monsters on the level containing the caster. You can also understand the types of the monsters.

Spellbook of detect treasure

Item Detect Magic Level 4

Displays all items on the same level as the caster. The general type of the items is also displayed, making it very useful when you want to obtain weapons or armor.

Spellbook of detect unseen

Invisibility Detect Magic Level 3

By casting this spell, you will be able to see invisible objects for a while. Use it when attacked by transparent monsters.

Spellbook of dig

Earthquake Magic Level 5

When this spell is cast, the walls of the dungeon crumble and passages are created. It can also be used on rock, turning it into countless small stones.

Spellbook of extra healing

Full Heal Magic Level 3

When this spell is cast, your hit points recover significantly. It is recommended over healing spells when you need more recovery.

Spellbook of finger of death

Death Touch Magic Level 7

When the caster casts this spell, a beam of death emanates from their fingertips. The target monster or person will die if they cannot withstand it. However, nothing happens if they can endure it.

Spellbook of fireball

Fireball Magic Level 4

A ball of fire flies out from the caster's palm and expands into a huge fireball, attacking the enemy. It is a typical offensive-type spell.

Spellbook of force bolt

Force Bolt Magic Level 1

A force field is emitted from the palm, dealing damage. While the damage dealt is small and the enemy may avoid it, it has the advantage of consuming less magic power.

Spellbook—

175


## Page 178

Spellbook of genocide

Genocide Spell
Magic Level 7

By casting this spell, you can completely exterminate one race from Yendor's dungeon. When using this spell, it is necessary to engrave the name of the race you wish to exterminate accurately.

Spellbook of haste self

Self Haste Spell
Magic Level 3

This spell can double the caster's movement speed, attack frequency, and other related attributes. It can be used during combat or when dealing with creatures that are too fast to catch.

Spellbook of healing

Healing Spell
Magic Level 1

This spell restores some hit points to the caster. It is quite useful right after entering the dungeon, but since severe injuries are common in deeper levels, it is not very effective.

Spellbook of identify

Identify Spell
Magic Level 5

This spell identifies unknown items. It has similar effects to scrolls, but the spell can be cast to identify items, making it more convenient to use.

Spellbook of invisibility

Invisibility Spell
Magic Level 4

By casting this spell, the body of the caster becomes transparent. The items the caster holds also become transparent, but once dropped, they will no longer be transparent.

Spellbook of knock

Unlock Spell
Magic Level 1

This spell can unlock doors and large chests that are locked. As long as the casting of the spell does not fail, it can open any lock without the risk of failure.

Spellbook of levitation

Levitation Spell
Magic Level 4

By casting the "levitation" spell, the caster can walk in the air. In Yendor's dungeon, most traps are set on the floor. This spell is the best means to avoid trap activation. However, note that you cannot pick up fallen items while the levitation spell is active.

176

ITEMS—The Tools Awaiting You in the Dungeon


## Page 179

Spellbook of light

Light Magic Level 1

Once this spell is cast, it can illuminate a room that is in darkness. The light from this magic will continue to shine without fading.

Spellbook of magic mapping

Magic Mapping Level 5

The caster of this spell will have a vivid sense of the map of the level they are on imprinted in their mind. The existence of altars or fountains can also be known.

Spellbook of magic missile

Magic Missile Level 2

This is a spell that produces and launches a beam of light. It is a basic attack-type spell, and mastering this spell serves as a sign that the mage has become proficient.

Spellbook of polymorph

Polymorph Level 6

This spell changes the caster or a monster's form. However, if the polymorph spell is cast upon oneself, one must be able to control the change in some way, or risk turning into a goblin or kobold. Therefore, caution is necessary when using this spell.

Spellbook of remove curse

Remove Curse Level 5

This spell removes curses from items. It allows one to release weapons that won't leave your hand or armor that you can't take off.

Spellbook of restore ability

Restore Ability Level 4

This spell restores diminished ability scores caused by drinking poison or angering a god.

Spellbook—Magic Book

177


## Page 180

Spellbook of sleep

Sleep Spell
Magic Level 1

This spell emits a sleep ray from the caster's fingertips. If this spell works, most monsters will no longer be enemies.

Spellbook of slow monster

Slow Monster Spell
Magic Level 2

A spell that reduces the speed of monsters by half. It has the opposite effect of haste self. It may be useful in some cases where haste self would not be.

Spellbook of teleport away

Teleport Away Spell
Magic Level 6

This is a spell that teleports the caster or an enemy monster. It might be a good idea to use this spell temporarily to escape combat when your hit points are extremely low.

Spellbook of turn undead

Turn Undead Spell
Magic Level 6

A spell that causes panic among beings whose life originates from death, causing them to flee from the caster. It is equivalent to the purification power of a cleric and can even destroy them in some cases.

Spellbook of wizard lock

Wizard Lock Spell
Magic Level 2

A spell that locks doors using magical power. Unfortunately, the effectiveness of this spell is not great, and it can easily be picked without much difficulty.

Tools and Miscellaneous Items

Welcome to Dibb's General Store. Oh, have we met somewhere before? Why, this is your second visit? How rude of me. What can I get for you? We handle everything from food to Excalibur. Well, Excalibur was in stock until recently, but unfortunately, we haven't received any new shipments lately. But we'll have more soon.

We're the only ones who deal with various small items and tools! Some of them might be useful for your adventures. Come and take a look. It won't cost you anything to enjoy the view.

178

Items—The Tools Awaiting You in the Dungeon


## Page 181

Bag of Holding

バッグ オブ ホールディング

A magical bag that no matter how many items you stuff into it, it will never exceed a certain weight. It is a desirable item for adventurers.

Bag of Tricks

バッグ オブ トリックス

A mysterious bag that produces monsters every time it is used. Be careful to distinguish it from the Bag of Holding as it can be mistaken for one without being enchanted.

Blindfold

目隠し

A mask-like blindfold. It would be particularly useful if you have telepathy.

Bugle

らっぱ

A military bugle. It's better not to blow it on floors where there are barracks. Also, in some places, knowing a certain note can be very helpful.

Chest

櫃

Usually found rolling around in a dungeon, but there's no reason why you can't carry it. However, it is quite heavy and has no particular advantage to carrying it around.

Credit Card

クレジットカード

A plastic card. It can be used to open locked doors by inserting it into gaps in chests or doors.

Crystal Ball

水晶球

A crystal ball ground into a perfect circle by magic. By looking into the center of this crystal ball, you can discover the whereabouts of various objects such as food, monsters, or gold coins.

Drum

ドラム

Like other musical instruments, it can wake up sleeping monsters. Monsters seem to be afraid of the sound of drums for some reason.

Drum of Earthquake

ドラム オブ アースクエイク

When this drum is struck, an earthquake of a magnitude corresponding to the character's skill level occurs. In some cases, it may also create several pits (pit).

Tools——道具

179


## Page 182

BAG OF HOLDING

CREDIT CARD

DRUM OF EARTHQUAKE

expensive camera

a high-priced camera

It is a high-priced camera. Of course, it comes equipped with a flash, so it can be used to blind monsters by setting it off.

figurine

フィギュア

A small statue. Using this statue will cause the same monster as the statue to appear, and it will serve as a obedient pet to the character. For example, using a red dragon statue will summon a red dragon as a pet, and using a nymph statue will summon a nymph as a pet.

fire horn

ファイアホーン

When this horn is blown, flames will erupt from its tip. Naturally, it can be used as a powerful weapon.

flute

フルート

In some place, playing a certain melody will be useful. Also, if the player is skilled at blowing the flute, they can tame snakes.

180

ITEMS—Dungeons await you with these tools


## Page 183

FIGURINE

frost horn

Frost Horn

When blown powerfully, this horn emits freezing rays from its tip. It can freeze water or defeat monsters.

harp

Harp

It is said to have the effect of taming mischievous fairies, but one must be dexterous to use it effectively.

horn

Horn

When blown, it wakes up any sleeping monsters on the same level. Additionally, this horn is said to play a sound that frightens monsters.

ice box

Ice Box

The weakness of monster corpses, except for a few, is their tendency to decay rapidly. However, by storing them in this ice box, decay can be prevented. Note that this box itself is very heavy, so those without strength would find it difficult to carry.

Tools—Tools

181


## Page 184

key

Key

Various keys. The type is indicated by the part you hold.

lamp

Lamp

Can be used to illuminate dark rooms. No other effects.

large box

Large Box

Similar to a sack, it can store items. However, it seems it has no advantage in carrying due to its considerable weight.

leash

Leash

Enables you to walk with your pet. In other words, you can treat your pet like an item. Even if it gets caught in a teleport trap, the pet will teleport along with the character.

lock pick

Lock Pick

Can open locked doors and large boxes. Many thieves prefer their own skills over credit cards or spare keys and cherish this lock pick.

magic flute

Magic Flute

The soothing sound of the magic flute can put many monsters to sleep.

182

ITEMS—Waiting for you in the dungeon


## Page 185

Magic Harp

Magic Harp

It is said that most monsters will be enchanted by the sound of the magic harp regardless of the player's skill as a musician.

Magic Lamp

Magic Lamp

A magic lamp. Of course, when rubbed, a spirit (djinni) will appear, and in many cases, grant a wish.

Magic Marker

Magic Marker

It becomes easy to engrave messages on the dungeon floor. It also has the ability to write desired spells on blank scrolls. The reason why it does not fade easily is because it uses "magic ink."

Magic Whistle

Magic Whistle

A magic whistle. If you have a pet, you will likely see your pet teleport to your side the moment you blow it.

Mirror

Mirror

A mirror. Some monsters seem to fear their own ugly appearance and avoid mirrors. It would also be effective against monsters that attack with gaze.

Tools—Tools

183


## Page 186

Pick-axe

A pick-axe. It can be used to dig holes in walls and crush rocks. While it can also be used as a weapon, it is recommended that you use another weapon if you have one. It is quite heavy, so carrying it will be difficult unless you have considerable strength.

Sack

A sack. The maximum number of items a character can carry is 52. However, by using a sack, you can store additional items, thereby being able to carry more than 52 items.

Skeleton Key

A magic key. It can automatically detect the shape of a lock and change its own shape accordingly.

Stethoscope

Use this on monsters or pets to gain detailed information about them. You can even know their symptoms if they are sick or confused. It is standard equipment for a healer (Healer).

184

ITEMS—Magic Dungeon Awaits You With These Tools


## Page 187

Tinning Kit

Can opener

A magical tool that makes it easy to open cans that take a considerable amount of time to open. Note that this tool is heavy.

Whistle

Whistle

Blowing this whistle will cause your pet to start moving towards you. However, other monsters will also become aware of the location where the whistle was blown, so be cautious.

Wands - Wand

Hello, glad to see you. Welcome to Dax's wand shop. What can I do for you? Even if you're not a mage, these wands can give you a taste of magic. There are even wands like "Wand of Wish" that can produce any item. Take your time and browse. Oh, and be careful with the "Wand of Nothingness." It has no power at all.

Wand of cancellation

Wand of Disruption Magic

This wand contains the power to nullify magical power. Monsters pointed at by this wand will lose their special abilities. For example, you can make a leprechaun lose its teleportation ability.

Wand of create monster

Wand of Monster Creation

It summons monsters. Useful when you don't have food.

Wand of cold

Wand of Cold

It emits freezing rays. When the rays hit a monster, they can deal significant damage.

Wands - Wand

185


## Page 188

Wand of death

Wand of death shoots a beam of death. All living creatures in the direction of the beam will die. However, it will deal no damage to creatures that have resistance to the beam of death.

Wand of digging

Wand of digging

This wand can dig holes within the dungeon. It can also be used as an effective attack against monsters that envelop and attack characters.

Wand of fire

Wand of fire

This staff produces a raging flame snake from its tip. It can deal damage to many monsters.

Wand of light

Wand of light

This staff produces a light ball. While it can brighten dark rooms, it has few other uses.

Wand of lightning

Wand of lightning

This staff shoots lightning. Since monsters with resistance to electricity are relatively rare, it is an effective means against most monsters.

Wand of locking

Wand of locking

This wand can lock doors, chests, large boxes, and so on.

Wand of magic missile

Wand of magic missile

This staff contains a missile spell. While its power is not great, it is effective at dealing sure damage.

Wand of make invisible

Wand of make invisible

When this staff is waved over a monster, it becomes transparent. In other words, using it on oneself will make one transparent.

Wand of nothing

Wand of nothing

This staff has no effect at all.

Wand of opening

Wand of opening

This wand can open locked doors and large chests.

Wand of polymorph

Wand of polymorph

This wand can transform monsters, pets, or even oneself. It can also transform items. 

186

ITEMS—Magic awaits you in the dungeon


## Page 189

If you wave it, you can transform any item into another.

Wand of probing

Identification wand

When waved at monsters or pets, you can learn their hit points, gold, and other characteristics.

Wand of secret door detection

Detection wand

When waved in a room, this wand can discover secret doors. Of course, if there are no secret doors, there will be no reaction.

Wand of sleep

Sleep wand

When waved at monsters, they can fall asleep. However, this does not apply to monsters that have resistance to sleep.

Wand of slow monster

Slow monster wand

When waved at monsters, it can cast the slow spell on them, halving their movement speed and attack frequency.

Wand of speed monster

Speed monster wand

It can double the target's movement speed and attack frequency when waved. Of course, it can also be used by the character itself.

Wand of striking

Striking wand

When waved at monsters or other targets, it can deal some damage. Additionally, it can also be used to destroy rocks (boulders).

Wands——Wands

187


## Page 190

Wand of Teleportation

Wand of dimensional jumping

Teleports to some place on the same level. If you have Teleport Control, you can choose where to teleport.

Wand of Undead Turning

Wand of purification

Has the effect of making undead creatures flee. Also has the power to resurrect corpses.

Wand of Wishing

Wand of wishes

When this wand is waved, it causes one item to appear. However, it is better to avoid wishing for a Wand of Wishing.

Weapons 武器

Well met! This is the shop of Kray's weapons. They deal in everything from swords to a single arrow. They will buy your discarded weapons at a good price. What would you like?

SWORDS 剣

The sword is the weapon that knights take pride in and samurais think embodies their soul. As a warrior, it should be your main weapon. Most are one-handed. It is also possible to increase your defense by holding a shield in your other hand.

Broadsword

Broadsword

The typical sword that comes to mind when we hear "sword." It is a basic equipment for knights. The blade length is about 1 to 1.5 meters. Compared to long swords, it is characterized by having a much wider blade.

Dwarvish Short Sword

Dwarfish short sword

Since dwarves are short, they cannot use long swords or spears. Therefore, they

188

ITEMS—The Tools Awaiting You in the Dungeon
SOURCE


## Page 191

He prefers to use short swords. However, if he is really a combat-oriented dwarf, he would use an axe.

Elven Broadsword
エルブン ブロードソード

An elven sword. The scabbard and hilt are adorned with intricate designs. Also, due to their delicate skills, the damage dealt to monsters is slightly greater than that of a regular broadsword.

Elven Short Sword
エルブン ショートソード

An elven short sword. Like the broadsword, it has a sharper edge than a regular one, albeit slightly.

Katana
カタナ

A curved sword considered mysterious by eastern warriors, samurais, who believe the souls of their ancestors are embedded within them. Made using a special steel-making technique, it is slender yet very sturdy, and its power greatly surpasses that of broadswords or longswords.

Short Sword
ショートソード

A sword about half the length of a longsword. Thieves and races with body types unsuitable for longswords prefer this weapon for its agility.

Long Sword
ロングソード

A longsword. Preferred by mercenaries and skilled warriors because it can be wielded with one hand, allowing the other hand to hold a shield for defense.

Two-handed Sword
ツーハンデッドソード

A greatsword meant to be used with both hands. Preferred by berserkers for their raw strength, more of a weapon to bash with rather than slash.

Scimitar
シミター

A curved sword favored by pirates. It can be swung down easily, giving it good maneuverability. There are also stories of orcs and ogres preferring to use it.

Orcish Short Sword
オーキッシュ ショートソード

A short sword used by lower-class orcs. It has many chipped edges and inferior material, resulting in less damage dealt.

Weapons—武器

189


## Page 192

KATANA

SHORT SWORD

TWO-HANDED SWORD

SCIMITAR

190

ITEMS—Magic awaits you in the dungeon


## Page 193

DAGGERS 短剣

It's better to think of daggers as secondary weapons rather than primary ones. Also, since they are easy to throw, there's no harm in carrying a few of them.

athame

アサメ

A short sword favored by mages. It is cast from very hard material, so it doesn't chip. It is very easy to handle, but its power is negligible.

crysknife

クリスナイフ

A knife with a blade length of about 20 centimeters made from meteor iron. Its power and sharpness are said to match those of a greatsword due to the magic within it.

dagger

ダガー

A short sword with a blade length of about 20 centimeters.

elven dagger

エルブン ダガー

A short sword beautifully decorated by elves. Used by races that are too short to wield swords, such as hobbits.

knife

ナイフ

A knife (did anything else come to mind?). One of the weapons you should consider throwing rather than using to hold.

orcish dagger

オーキッシュ ダガー

A short sword favored by orcs. It is likely the most commonly available weapon in Yendor's dungeons. Its power can be guessed.

scalpel

メス

A surgical scalpel. It is a weapon that healers start with, but it's best to switch to another weapon as soon as possible.

wakizashi

ワキザシ

A short sword used as a katana's auxiliary weapon by warriors from the eastern islands. Although it is a short sword, it boasts considerable power.

Weapons—武器

191


## Page 194

STAFFS Wands

Staffs are not favored by spellcasters without vitality. Or, it seems that clumsy barbarians or ogres use clubs.

aklys

Aklys

A club reinforced with wire wrapping or sharp metal pieces inserted between the wires to increase its power. It is said that ogres prefer to use this.

club

Club

A short wooden stick. A person with strength can deal decent damage with it, but it is not a reliable main weapon.

flail

Flail

A development from agricultural tools, a connected club. It consists of a handle part and a striking part connected by a chain or metal ring. It utilizes centrifugal force, allowing even those without much strength to deliver considerable power.

192

ITEMS—Dungeons await you with these tools


## Page 195

Mace

A metal club. The striking part is knobby, and spikes are often attached to this part to increase its power. It is sometimes called a maul.

Morning Star

A ball of iron connected to a club by a chain. It can be said to have the highest power as a weapon that is struck. Named so because the spiked iron ball looks like a morning star.

Quarterstaff

A wooden staff. Often favored by wizards. However, the staff martial art, which uses this staff to confuse and fight the enemy, is a school of combat.

Weapons—武器

193


## Page 196

AXES

Weapons for knocking down opponents who are not wearing armor. Many can also be used in everyday life.

axe

Axe

An axe. At times it can boast power equal to, or even greater than, a sword.

dwarvish mattock

Dwarvish Mattock

A pickaxe-like axe. It is said to display tremendous power when swung with force by dwarves, who are small in stature.

war hammer

War Hammer

A hammer with its tip sharpened. It is not a huge maul.

194

ITEMS—Dungeons await you with their tools


## Page 197

SPEARS 棍

Can be used as a throwing spear and also in close combat, making it a versatile weapon. It has decent power and isn't too heavy, so carrying it as a secondary weapon isn't a bad idea.

dwarvish spear

Dwarvish Spear

A shining spear made by dwarves. Given that its tip is made of mithril silver, it boasts one of the highest attack powers among spears.

elven spear

Elven Spear

An elven-made spear. Runes are carved all the way from the handle to the tip.

javelin

Javelin

A slender spear. Primarily made for throwing, it's not suitable for close combat.

lance

Lance

A cavalry spear. Usually used by mounted attackers for charge attacks, but there are lances for infantry as well.

orcish spear

Orcish Spear

A black spear favored by orcs. Like other weapons made by orc hands, its power is inferior to other spears.

spear

Spear

A basic spear. Length varies, but those around 1.5 meters to 2 meters long are referred to as spears.

trident

Trident

A trident with three-pronged tips. Originally used for catching fish in water. Its ease of handling is a notable feature.

Weapons—武器

195


## Page 198

BOW & ALLOW 弓矢

Using a bow shoots arrows, and using a crossbow shoots bolts. Arrows and bolts can also be thrown by hand, but the power when shot from a bow is incomparable to that. After all, arrows are meant to be shot from a bow.

bow

弓

Use this to shoot arrows. It can be said to have the greatest power against small creatures. Additionally, you can use a bow as a melee weapon to strike enemies, though it is not recommended. 

196

ITEMS—Dungeons awaiting you with their tools


## Page 199

orcish bow

Orcish Bow

A shortbow that orcs are known to use. Among the three types of bows, it has the weakest power. This is due to the poor quality common to items made by orcs.

elven bow

Elven Bow

An arrow made by elves. It is engraved with fine runes, which increases its power compared to a regular bow.

arrow

Arrow

A plain arrow. It can be thrown, but its power is significantly weaker when used with a bow compared to other arrows.

silver arrow

Silver Arrow

An arrow with a silver tip or silver-plated. Silver, which possesses holy power, is effective against demons and ghosts and similar monsters. 

Weapons—Weapons

197


## Page 200

orcish arrow

Orcish Arrow

A black arrow made by orc craftsmen. Compared to other arrows, it can be said to be of rather poor quality.

elven arrow

Elven Arrow

An arrow made by elven craftsmen. Runes are also engraved on this one.

crossbow

Crossbow

A crossbow. It consists of a wooden stock and a bow at a right angle, unlike a bow, and its characteristic is that it is used to shoot. Its power far exceeds that of a bow, but its weakness is that rapid fire is impossible.

crossbow bolt

Crossbow Bolt

An arrow for a crossbow. Also called a quarrel. While it can be thrown, it goes without saying that using a crossbow is better.

POLE ARMS ポールアーム

Pole arms are weapons with a long pole and an axe or spear attached. They cannot be used with one hand, and their biggest weakness is that shields cannot be used simultaneously. However, they do boast a certain degree of power.

bardiche

Bardiche

A large weapon like an axe that was commonly used in northern empires. It was basically used in the same way as an axe.

bec de corbin

Beck De Corban

A warhammer with a long handle, meaning "bird's beak". It was commonly used in the eastern subcontinent.

bill-guisarme

Bill-Guisarme

A guisarme with a pick-like head.

fauchard

Fauchard

A great scythe carried by a death god in paintings. Hooks are often attached to it.

198

ITEMS—Dungeons awaiting you with their tools


## Page 201

Glaive

グレイブ

A polearm with a knife-shaped blade at the end. In the eastern islands, it is called a naginata and is favored as an armament by women and girls.

Guisarme

ギザルム

A type of glaive. The characteristic feature is that it has a blade much larger and more curved than a glaive. In many cases, a hook is attached to the reverse side.

Halberd

ハルバード

A polearm combining a long spear blade with an axe. It can be used for cutting, thrusting, and sweeping.

Lucerne Hammer

ルッツェルン ハンマー

A type of long pickaxe. In some places, it is the same as a bec de corbin.

Weapons—武器

199


## Page 202

As it is sometimes treated.

partisan

パルチザン

A type of spear with a fan-like unique blade protruding from the base of the spearhead.

ranseur

ランサー

An armed weapon with a long pole and a very long, thin blade attached to the tip. In many cases, two blades extend horizontally from the base of the blade.

spetum

スペタム

A two-pronged spear with a very long handle. Effective against large enemies.

voulge

ヴージ

A long pole with an axe-shaped cutting edge attached to the tip. Primarily a slashing weapon, but can also be used to stab.

200

ITEMS—Dungeons awaiting you
SOURCE


## Page 203

OTHERS OTHERS

There are weapons that don't fit within the scope I've talked about so far. Well, there are many items with various characteristics, so there might be some usable ones depending on the situation.

boomerang

ブーメラン

A weapon favored by the indigenous people of the southern continent. If you are dexterous, it can return to the thrower's hand if it doesn't hit the enemy.

bullwhip

鞭

Made from woven animal hide. Its lightness is an advantage, but the damage it deals is negligible.

dart

ダーツ

While more suitable for games, this is a larger dart. You can fight with it, but throwing it would probably be more practical.

rubber hose

ホース

A rubber hose. The purpose of its existence is not well understood.

shuriken

手裏剣

A star-shaped throwing knife (throwing star). It seems that samurai warriors from the eastern lands prefer to use it.

sling

スリング

A weapon used to throw stones lying around. The method of use is similar to a bow and arrow, but its power is not particularly great.

BOOMERANG

DART

Weapons—武器

201


## Page 204

Worm Tooth

A longworm's fang. It is resistant to acid and rust, so it might be useful against monsters with such characteristics. It is a two-handed weapon.

Named Weapons

Weapons that have been granted by gods or have lain dormant in some corner of this dungeon. Due to their incredible quality, each weapon has a name. Well, you've probably heard of a few of them.

Cleaver

A great axe with a magnificent blade. Details are unknown, but it is known that its attribute lies in the chaotic realm.

Demonbane

Demonbane—Demonbain

A longsword that unleashes its greatest power only against demons. It is said to be forged by a swordsmith who lost his beloved kin to demons, trading his life for the sword.

Dragonbane

Dragonbane—Dragonbain

A sword that boasts great power only against dragons, created solely to slay their lairs.

Excalibur

Excalibur

A legendary longsword that can only be wielded by those whose worthiness is recognized by a lady from a holy spring. Those who hold it are said to gain unmatched power.

Fire Brand

Flame Sword—Firebrand

A longsword with a blade wrapped in flames. Those who carry this sword are said to gain resistance to fire.

Frost Brand

Ice Sword—Frostbrand

A longsword with a blade constantly encased in frost, clear as ice. Those who wield the Frostbrand are said to gain resistance to cold.

202

Items—The Tools Awaiting You in the Dungeon


## Page 205

STORMBRINGER

FIRE BRAND

FROST BRAND

EXCALIBUR

Giantslayer

Giantslayer——Giant Slayer

A long sword said to wield great power against giants such as the Giant Race, Minotaur, and Owlbear.

Grimtooth

Grimtooth

A short sword forged from the teeth of the hero Grim, as it is told among the Ogres. It has no particular features but is very easy to use.

Mjollnir

Mjölnir——Thor's Hammer

A warhammer that can emit lightning. It is rumored that it returns to your hand when thrown, but this is uncertain.

Ogresmasher

Ogre Slayer——Ogre Smasher

A warhammer forged with the sole aim of defeating Ogres. It harnesses the power of solar light.

Weapons——Weapons

203


## Page 206

It seems to possess great power against ogres due to being sealed in a different manner than theサンソード.

Orcrist

Chomping Blade——Orcrist

This great sword, known as Orcrist among elves and feared as Chomping Blade among orcs, has been a renowned blade that has cut down hundreds of orcs.

Snickersnee

Snickersnee

This katana, a legendary blade that samurai dream of holding once, will cleave whatever touches its blade in two.

Sunsword

Sunblade

A longsword said to have the power of life—light of the sun sealed within its blade. It is natural that it would possess supreme power against beings that hold the source of life in the realm of death.

Sting

Piercing Blade

This elf-made short sword, wielded by some hero named Bilbo or perhaps a hero named Thorin, shows great power against orcs and warns the wielder of the danger that orcs pose before it.

Stormbringer

Stormbringer

Those who touch this sword's blade are said to lose their vitality to the sword and vanish. The first person to wield this sword sustained his life by feeding on the vitality he had stolen with the sword, though the truth of this is unknown.

Trollsbane

Trollbane

A morningstar created to crush trolls, with its striking part covered in mithril silver to inflict pain upon trolls.

Werebane

Werewolfbane

A longsword made to hunt beastmen. Some say there are swords that ring their blade to warn of the presence of beastmen, but this is unconfirmed.

204

ITEMS——Tools waiting for you in the dungeon


## Page 207

Preface Copybook·Dungeon Ecology Museum

The monsters described here are detailed accounts of the grotesque creatures believed to lurk in Yendor's dungeon. They are either summoned there by amulets for protection, have somehow taken up residence in Yendor's dungeon, or have been warped by too much magic in Yendor, causing them to wander into the dungeon from elsewhere.

After many years of research, several chroniclers have finally compiled this information into a single book titled "Dungeon Ecology Museum." This comprehensive work is being sold for 1000 zmarks to adventurers who wish to enter Yendor's dungeon. Here, we present a copybook containing only the most important information extracted from this book.

However, the monsters listed here are not all the creatures that lurk in Yendor's dungeon. Furthermore, not everything described in this book is necessarily true. It is your task to explore Yendor's dungeon and see for yourself.

Editor/Ceridia Foren

Monsters Preface

Page 205


## Page 208

A Ape, Carnivorous Ape

Ape (ヒヒ) is a large primate that can reach several meters in length. Originally omnivorous, it sometimes attacks adventurers to eat their flesh.

Ape often forms a group led by a boss. So even if one is defeated, there may be several more behind. It's a dangerous opponent when its strength is low. It's better to avoid fighting in open areas and lure it into narrow spaces. However, given that the ape's weapons are just weak claws besides its teeth, it shouldn't pose a significant threat to adventurers equipped with proper gear.

Also, the carnivorous ape (carnivorous ape) is a special classification of apes that were originally omnivorous but have become more ferocious due to long-term meat consumption, resulting in a body size nearly twice that of regular apes. In particular, those living in Yendor's dungeon seem to particularly enjoy eating human flesh, so adventurers should be cautious. However, they rarely act in groups and often wander alone like lone wolves, making them easier to defeat than regular apes in a general sense.

The meat of the ape is quite delicious among the monsters found in Yendor's dungeon. At least, it is at least dozens of times tastier than goblin meat.

B Bat, Giant Bat, Vampire Bat

These bats inhabit the dark dungeons of Yendor. Although the dungeon was created by Yendor and its subordinates, it seems they have taken up residence on the surface over time.

They attack intruders who are impolite by lunging with their small fangs to defend their territory. However, they don't have much strength, so they can be easily repelled. However, their behavior lacks consistency, so this part should be noted. They may approach and then retreat, or retreat and then approach, making it difficult to aim at them.

Additionally, the vampire bat is basically the same as the giant bat, but it has venomous fangs. According to rumors, the vampire bat might be the form taken during vampiric transformation. This is the vampire bat.


## Page 209

It is clear that the rumors arose due to the faster healing of these bats compared to other bats.

C Centaur

plain centaurs, forest~, mountain~

The centaur is a half-human, half-horse archer whose upper body is human and lower body is horse-like. When one thinks of a regular centaur, as mentioned above, it refers to those with a horse's lower body, but there are also centaurs found with only two hind legs as horse-like, while the other two legs are human. This might be some kind of deformity.

Moreover, in different lands, there are centaurs with lion-like lower bodies called Leon-tauri, and those with donkey-like lower bodies called Ono-tauri. Occasionally, there are even centaur-like creatures with a human upper body and dragon-like lower bodies known as Draco-tauri. To distinguish these rare breeds, the original centaurs are sometimes referred to as Hippocentaurs.

In Yendor's dungeon, reports of plain centaurs (plain centaur) living in grasslands, forest centaurs (forest centaur) living in forests, and mountain centaurs (mountain centaur) living in mountains have been made.

It is believed that centaurs were creatures who loved nature, but why they settled in Yendor's dungeon is not well understood.

Their main weapon is the bow and arrow, but when engaging in close combat, they can deliver powerful kicks from their horse legs. If you defeat them, you can obtain a longbow and several arrows.

D Dragon

unknown? (unknown existence)

Dragons (Dragon) are not legendary beings born in children's bedtime stories. Already, several types of dragons have been confirmed in the deepest layers of Yendor's dungeon. However, very few survivors have returned from seeing them, and even those who did return do not speak about them, fearing their existence. Therefore, only very limited information is known.

Firstly, the type of dragon seems to be determined by the color of its scales. And depending on the color of these scales, the breath of the dragons changes. This is called "dragon's breath" and can consist of concentrated acid, toxic gas, freezing liquid, etc., which they exhale from their mouths. So far, the abilities of the confirmed dragons are limited to this.

Furthermore, their strong claws and fangs are said to pierce even plate mail. More detailed abilities are unknown.

Huh, bats, centaurs, dragons

207


## Page 210

vampire bat

centaurs

fire elemental

dragon

carnivorous ape


## Page 211

It can be said that the necessity for further research is very high.

Moreover, it has been confirmed that they are oviparous. Young dragons found at shallower levels are likely unable to withstand the fierce struggle for survival in the deeper layers, having hatched from eggs. Young dragons cannot breathe fire and are often repelled by adventurers using their claws alone. The scarcity of dragon growth stages might also be due to such reasons.

Furthermore, there is a legendary blade forged solely for the purpose of defeating dragons, waiting to be wielded by someone in some corner of Yendor's dungeon.

E Elemental (Spirit) water elemental, fire elemental, earth elemental, air elemental

Elementals refer to the elements of this world. That is, fire, water, wind, and earth. However, in this case, elementals are not such conceptual beings. They are pseudo-life forms generated from these elements. Originally, these spirits would merely exist in the spirit realm, passing their days in tranquility as creators of the world. But due to being dragged out of the twisted dimensions of Yendor's dungeon by powerful magic, they too have become distorted spirits, monsters that confront humans—spirits turned into monsters.

As great beings wielding the pure essence of the elements that sustain the world, they will stand as formidable opponents before adventurers. There are those that scatter intense heat when struck with a sword, and others that can engulf adventurers within their bodies, dealing massive damage.

However, details about mad spirits are largely unknown outside of Yendor's dungeon, as sightings of such entities are rare.

F Slime Viscera Violet fungus, brown mold, yellow slime, green slime, red slime

Several lichens and fungi grow in Yendor's dungeon. Occasionally, they can be found in abnormally dense clusters. Particularly, giant molds do not attack unless provoked. They merely exist there.

However, if an adventurer initiates an attack, they will suffer a devastating counterattack. Giant molds possess the ability to scatter spores within their bodies upon impact. These spores contain highly acidic substances that adhere to living skin.

Elementals. Slime Viscera

209


## Page 212

And there are said to be things that emit abnormal heat. Therefore, it might be the best method to ignore them when you find mycelium. However, there are also mycelium that can withstand attacks from spores if you defeat and eat them. They might be worth considering rather than ignoring.

Moreover, among the mycelium, the violet fungus seems to have a slightly different nature. This organism, although a mycelium, can move on its own and even communicate with us! It might be something like a matango...

G Gnomes

gnome, gnome lord, gnome king, gnomish wizard

Gnomes are said to be humanoid relatives of dwarves. Like dwarves, they form clans and often dig holes in the earth to build comfortable dwellings where they live. They are generally about one size smaller than dwarves and many possess the qualities of brave warriors.

It is unknown why they reside in Yendor's caves. Perhaps they are repelling intruders as a thank you to Yendor for providing their ideal habitat.

Just as with humans, there are various types of gnomes. There are good gnomes and evil-hearted gnomes. In the same way that there are humans serving as guardians of Yendor, there are gnomes doing the same.

While gnomes themselves are not formidable foes, the gnome lord (gnome lord) who unites the clan or the gnome king (gnome king) who oversees the gnome lords are quite formidable enemies. Additionally, there are gnomish wizards who can use magic, but it seems they are not particularly skilled in this regard.

H Giants

giant, stone giant, hill giant, fire giant, frost giant, minotaur, owlbear, ettin, titan

They are collectively called 'giants', but each has a different nature. Let's explain them by dividing them into several groups.

● GIANT

First, let's discuss the so-called 'giant giants'. Those called 'giants' are humanoid beings similar to humans or elves, simply with a larger physique.


## Page 213

It is not long ago.

In modern times, they rarely appear in public, so they are treated as legendary creatures, but this is a mistaken understanding. 'Giants' include common giants (giant), stone giants (stone giant) that prefer rocky areas, hill giants (hill giant) that inhabit hilly regions, fire giants (fire giant) that live in tropical or volcanic areas, and frost giants (frost giant) that inhabit cold regions. Their forms can be seen in Yendor's dungeons as well. Although they love nature, it is unclear why they choose to reside in Yendor's dungeons.

Moreover, it is rumored that eating their meat will transfer their abilities to the eater. They are said to gain extraordinary strength.

● MINOTAUR

Minotaurs (minotaur) are half-human, half-bull monsters. They dwell in labyrinths and caves, boasting monstrous strength with which they can cleave adventurers in half with their huge axes. They have low intelligence and are violent, making them one of the most troublesome opponents for adventurers.

● OWLBEAR

Owlbears (owlbear) are monsters created by ancient magic from a combination of bears and owls. They strangle their enemies with their powerful bodies and then suffocate them. If you encounter an owlbear in Yendor's dungeon, it would be wise to forget about running away.

● OTHER GIANTS

Also, titans (titan) are said to be descendants of ancient gods, but the details remain shrouded in mystery, and are entirely unknown. The same applies to ettins (ettin).

I Stalker

Stalker

A stalker (stalker) is a demon summoned from another dimension by sorcerers. They obey Yendor's commands until the moment they vanish, standing in the way of adventurers.

Their greatest feature is that they are transparent (invisible). In many cases, their first strike is a surprise attack on adventurers. Even after realizing they have been attacked, it is difficult to fight them because it is impossible to see where the stalkers are.

Gnomes. Giants. Stalkers

211


## Page 214

gnome

minotaur

giant

jabberwock

guardian

YUKI / HIRO

YUKI / HIRO


## Page 215

It would be a truly terrifying invader. One could say it is a fearsome attacker.

However, being transparent means nothing in front of elves' astonishing vision. Those who have gained the ability to 'see invisible' by some means can see their form.

There is also a rumor that eating a stalker's flesh can make one transparent. This comes with considerable danger, as the effects of consuming meat from an extradimensional life form are entirely unknown.

J Jabberwock

A mysterious existence. It seems to be a monster with considerable power, and its sightings are extremely rare, making the Jabberwock a mysterious entity.

From limited sightings, it appears to be a creature somewhat similar to a dragon. It has wings like a dragon and is almost certainly capable of flying. Its claws and fangs are extremely sharp, suggesting it is carnivorous and may attack humans as well. It is also said to possess excellent vision, with its eyes glowing like flames.

Limited sightings on land report it emerging from forests, swaying slightly. Some also report it approaching with a sound like bubbles rising to the surface.

In summary, while there are a few sightings, the actual ecology and personality remain unknown. The illustration in this book is merely an imagined depiction, and the true appearance is unknown. However, if you encounter a dragon-like creature with sharp teeth and claws, consider it a formidable opponent.

K Keyston Kop, Kop Sergeant, ~Lieutenant, ~Kaptain

Watchmen are those who guard stores in the dungeons of Yendor and are contracted with them. They exist to make unscrupulous shoppers who attempt to steal valuable items from the store pay the price. If an alarm rings in the dungeon, be cautious, as it means watchmen have appeared at the request of the store owner. As long as a criminal is present, they will pursue relentlessly from wherever they appear.

Jabberwock. Watchman

213


## Page 216

The guards come carrying cream pies in one hand and rubber hoses in the other. By throwing the terrifying cream pies to blind the culprit, and subsequently punishing them with the terrible weapon of the rubber hose for the great sin of shoplifting, they aim to incapacitate the thief.

However, if the shoplifter sincerely repents and pays compensation to the store owner, they might (with a grudging nod) simply vanish. It goes without saying that their disappearance will be as sudden as their appearance.

Lich, demi-, master~

Liches are collectively referred to as those who obtained eternal life through ancient magic or became immortal through the power of a malevolent deity. Their cursed life spans half in the realm of death and the other half in the mortal world, making their souls immortal in the mortal realm.

By wielding the strong will to manipulate the forbidden art of immortality, liches have achieved a formidable magical power. Due to their immortality, they spend aeons studying magic, and as a result, they can control all forms of magic, summon storms, and create infernos.

Anyone who touches their bodies is drained of their essence due to the overwhelming power of their spirit, and everything touched by their fingers is cursed. In the depths of Yendor's dungeon, liches are among the most feared beings.

As mentioned earlier, liches hold half of their existence in the realm of death. Therefore, it is said that they cannot be injured by ordinary weapons, and only weapons imbued with magical power can harm them.

M Mummy

Mummies are the resurrected bodies of those who were buried but still harbored attachments to this world. Alternatively, there are local traditions where corpses are preserved in such a way that they revive after a certain period following death. However, if the resurrection fails, these mummies turn into monsters and attack people.

They hate the souls of the living that they could not obtain, and thus attack all living beings. They target kobolds, gnomes, orcs, elves, humans, ettins, and giants.

214

MONSTERS—Monsters wandering the dungeon


## Page 217

Such races that become mummies retain their power as they did in life. However, it is sometimes discovered that giant mummies have the same power as they did in life, that is, they boast a huge physique and an abnormal amount of strength. Special attention should be paid to mummy ettins and mummy giants.

In Yendor's dungeon, mummies seem to be produced by the magic of that sorcerer. It is impossible to think that only mummies resulting from怨恨or failure in corpse regeneration would exist in such great numbers wandering around the dungeon.

Moreover, those who die while wearing bandages obtained by destroying them become mummies.

N Naga

red naga, black naga, golden naga, guardian naga
red naga hatchling, black naga hatchling, golden naga hatchling, guardian naga hatchling

If you encounter a terrifying monster with the upper body of a human woman and the lower body of a snake's torso, it is a naga (naga). The color of the scales distinguishes the race, and there are some similarities between nagas and dragons, such as the ability to breathe dragon breath, which is very interesting. There is even a theory that nagas branched off from the lineage tree of dragonkind. It has been confirmed that nagas lay eggs, and several naga hatchlings have been found in the middle layers of the dungeon. Like dragon hatchlings, naga hatchlings cannot use their special abilities and seem to use only their young fangs as weapons.

It has also been confirmed that there are nagas that spit venom, nagas that conceal paralyzing poison in their fangs, and nagas that can wield magic. Those that breathe fire are said to have red scales, but the details of the other nagas' ecology remain unknown. Most of these characteristics are based on sightings alone, so approach with caution.

In Yendor's dungeon, the existence of nagas has been confirmed from the middle layers to the deeper layers. Guardian nagas (guardian naga) are known to be powerful beings, but due to their deep location, many details remain unclear.

O Ogres

ogre, ogre lord, ogre king

A man-eater. That is what an ogre (orge) is. There is no more accurate term to describe it. Its physique surpasses that of a human's by far, and its arm thickness is as large as an adult's torso. It boasts such strength that it can easily knock down a human with a single punch.

Ritchi, Mummy, Naga, Ogre.

215


## Page 218

Lich

Mummy

Orge

Yeki / Yiro

Yeki / Yiro

Black pudding

Naga

Yeki / Yiro


## Page 219

Orgs are known to wrap themselves in tattered loincloths and wield clubs, though they do not particularly favor clubs; it is said that this is because their fingers are clumsy and clubs are the only weapons they can manage to hold. However, scholars who have succeeded in closely observing orgs have unfortunately consumed all of their findings, leaving the details unknown.

They are carnivorous, and especially enjoy eating human flesh. It is not uncommon for them to bite off a live person's head. Orgs eat humans as if they were vegetables. Their sharp teeth regenerate when broken, and they never run out of teeth throughout their entire life.

In Yendor's dungeons, their existence is confirmed relatively near the surface, unlike oaks, and they often act alone. They can speak, but do not possess much intelligence. Provided they have sufficient strength, adventurers should not be threatened by them.

However, it is occasionally observed that they form clans, with leaders or kings existing within these clans.

P Slime-like Creatures

gray ooze, brown pudding, black pudding—

Gray Ooze (gray ooze), Brown Pudding (brown pudding), and Black Pudding are known as dungeon cleaners. They ingest and digest dead bodies, weapons, and armor left behind by adventurers. Gray Ooze and Black Pudding can dissolve metal items like swords and plate mail, while Brown Pudding ingests leather and cloth. There are rumors of places where these creatures are kept in garbage dumps for this purpose. However, they sometimes undergo abnormal proliferation and become uncontrollable, so caution is advised.

Basically, slimes lack anything that could be called intelligence and are merely living entities. However, when they 'exist' in the direction of an adventurer's progress, combat is inevitable. When forced to fight, avoid using corrosive weapons. Weapons made of materials that rust or rot will corrode and blunt upon impact with these slimes. Additionally, they have resistance to acid, poison, and cold, making them very difficult to defeat. However, many slime-like creatures are weak against fire. Using magic fireballs or a wand of fire would be effective.

Slime-like Creatures

217


## Page 220

It is meaningless to close the door when trying to escape from slime threats. Since slimes are amorphous creatures, it has been confirmed that they flow through the gaps in the door.

Q

Quantum Mechanic

A human who manipulates a system of magic that does not fit within any known magical concept. Those who have touched them have reportedly been flung through space and moved to some unknown place. However, it is certain that this is not a form of time-space transcendence as we know it. The method by which they do this is unknown to us, but they seem to possess and utilize the laws of this world constructed by their hands.

The reason why quantum mechanics exist in Yendor's dungeon is completely unknown. There are rumors that they are conducting some kind of experiment in the dungeon. It is said that their bodies are constantly contaminated by toxins from heavy metals due to long-term experiments. Therefore, eating the bodies of quantum mechanics may be extremely dangerous.

R

Rust Monster

Slightly larger than humans but moves quickly. It has dark brown skin and eyes that resemble emeralds. This monster's food is metal. It is rumored that steel is its favorite, but this has not been confirmed. It is also said to swim gracefully in water, but these claims have not been verified.

According to one adventurer, metal weapons and armor are ineffective against this monster. Its skin is said to have the ability to oxidize all metals. An adventurer witnessed a sword that had just been sharpened an hour ago rusting instantly upon being struck. Another adventurer saw a spear corrode upon touching the monster's skin.

Defense is similar. It is said that merely touching the tentacles growing from its head can cause metallic armor to deteriorate. Since it lacks fangs or claws, it does not attack to inflict wounds on the body, but the defense of armor and helmets is reduced, making it disadvantageous when fighting other monsters.

As for attacking methods, there is no option but to use weapons and armor that do not deteriorate at all.


## Page 221

There shouldn't be any.

This monster's reputation among adventurers is quite bad. It seems that they don't like its indirect bullying attitude. That's reasonable.

S Snake

snake, garter～, water moccasin,
pit viper, cobra, python

Snakes have been hated in this world since ancient times. The exact reason is unknown, but according to legends, they played a significant role in driving humans out of Eden. A certain god, enraged by the destruction of Eden, cursed snakes. There is also a legend that because of this curse, snakes lost their limbs and had to survive in a strange form. Whether the facts are as such, or whether it was a god and an immortal "saint" who survived from that time, no one knows.

In any case, snakes and their kind are despised and considered heretics in the world. They might be the closest existence to Yendor in some sense.

Snakes exist throughout the dungeon and attack from various places. Sometimes they hide under items or boxes in the dungeon and attack as soon as an adventurer touches them. Their attacks mainly consist of fangs and the poison they deliver through those fangs. According to adventurers, attacks from fangs cause little damage, but the poison is terrible. Without the ability to counteract, many died in agony from snake venom. It cannot be underestimated as a monster, even though it may seem insignificant.

T Troll

troll, ice～, rock～, water～, Olog-hai

A kind of giant. Various types of trolls are confirmed to exist in the dungeon, from ordinary trolls (troll) to water trolls (water troll) that drag adventurers underwater, ice trolls (ice troll) that are as cold as ice, and rock trolls (rock troll) that smash walls. 

It is said that Olog-hai (Olog-hai), which were granted mysterious magical powers by dark sorcerers, roam around, but there are no official reports about them. They are cruel and consider eating raw flesh the greatest pleasure. Their only weakness is that they turn to stone if exposed to direct sunlight, but there is no hope of sunlight in the dark dungeon.

They are immortal beings. Even if you manage to defeat them, you must properly dispose of the body.

Quantum physicist. Oxidation monster. Snake. Troll

219


## Page 222

rust monster

quantum physicist

troll

umber hulk

cobra

YUKI HIRO


## Page 223

In almost all cases, they will stand up and attack repeatedly. If you have reached a certain level and have adequate weapons and armor, you can feel secure. However, for inexperienced adventurers, it is still dangerous. If you manage to defeat a troll, it would be better to eat its corpse as soon as possible or escape before it revives.

A troll's weapon is its claws and fangs. The claws can be defended against if you have sufficient armor, but the fangs can inflict unexpected injuries on the adventurer. If you fail to dispose of the corpse and continue to be attacked, you may suffer from excessive bleeding, so caution is needed.

U Amber Halk

umber hulk

A large man with brown skin. Details about his appearance are unclear.

Reports about this monster are few, but one common point is that "be wary of their gaze." The severity varies among the reports, but those who are stared at by them tend to be overwhelmed with self-deprecating thoughts. They begin to question why they are fighting this monster, why they are in such a place, why they descended into the dungeon, and ultimately, why they are alive. What are they trying to achieve?

The theme of why one is alive might be something an adventurer contemplates once in a while. However, holding such thoughts in front of a monster is dangerous. The adventurer may become confused and unable to act normally, potentially suffering serious injuries. Caution is advised.

Apart from the gaze, they seem to attack with claws and fangs, but the effects of these attacks are unknown. Adventurers being attacked by the monster are in a state of confusion and cannot accurately strike back.

V Vampire, ~Lord, Vlad the Impaler

Vampire (vampire), lord vampire, Vlad the Impaler

Unlike other monsters, vampires are not summoned or enhanced by Yendor through magic. It seems they appeared from the eastern desert and settled in the dungeon when the demonic creatures under Yendor began to gather there. Of course, they show respect to Yendor and follow his commands, but they are not his subordinates; they are treated more like guests. They are a unique presence within the dungeon.

They are taller than humans by one or two heads. Their movements are agile, and they can easily dodge clumsy attacks. Their weapons include claws, but their most formidable weapon is

Amber Halk, Vampire

221


## Page 224

It is indeed fangs. They gain vitality by drinking the blood of adventurers.

An adventurer bitten on the carotid artery suffers not only physical injuries but also mental damage. Their accumulated mental energy is stolen through continuous combat. Mental energy encompasses not just spiritual elements like experience and knowledge, but also the vitality that sustains the body. To have one's energy drained means that the adventurer's abilities will decline.

To guard against vampire attacks, one must prepare items they are weak against, as these items are passed down orally and are strictly forbidden to be written down.

In the hierarchy of vampires, those belonging to a higher rank must unconditionally obey the commands of those above them. Vampire Lords (vampire load) are among the upper echelons of vampires. They are stronger than other vampires and possess greater magical abilities. According to rumors, there may exist a vampire that surpasses even the Vampire Lord, but their true identity has yet to be confirmed.

W  Wraiths

Barrow wights, wraiths, Nazgul

Wraiths are among the very dangerous entities in the dungeons of Yendor. Although their true form remains unknown, their intelligence has been confirmed by several reports. Adventurers have witnessed wraiths attacking prey with a sinister smile. Some say that they were the resentful spirits of those who died without being able to fully die. The resentful spirits trapped in the dungeons of Yendor sometimes take over the bodies of buried kings, and at other times, the resentful spirits themselves materialize to block new adventurers.

The power of resentment is formidable, and even experienced adventurers cannot guarantee their safety despite taking all precautions. Just touching a wraith or having their sword graze an arm can result in the draining of the adventurer's accumulated energy through continuous combat. Arms tremble, strength diminishes. Many adventurers shrink in size, and white hair appears in their hair.

Furthermore, some wraiths can summon strange mists to induce sleep in adventurers or cast spells to inflict wounds upon them.

To fight wraiths, adequate equipment is essential. "If your equipment is insufficient, run away. You should not engage in battle with wraiths until you have absolute confidence. Otherwise, you will be taken in by the wraiths and unable to achieve reincarnation," reads the blood-written text in the training manuals of the adventurer's school.

222

MONSTERS——Monsters that wander the dungeons


## Page 225

X Thon

xorn

A mysterious monster.

While not as powerful as dragons, the lack of information about them is extraordinary compared to ordinary monsters. The only things that are certain are that their weapons are claws and fangs, and they have incredibly thick skin. Beyond that, reports and rumors are relied upon.

Reports regarding their ability to pass through walls are included among the unreliable ones. According to one adventurer, they possess the ability to pass through walls. He was resting in a room to heal his wounds, and the room had only one door, which was locked. There were mechanisms set up so that if the monster tried to open the door, it would trigger and alert him to the presence of the monster. Thus, he rested in peace. However, Thon interrupted his rest. Fortunately, he managed to escape before making eye contact with Thon, so he did not suffer fatal injuries. Nevertheless, it remains unknown how Thon entered and attacked him, as he opened the only door when fleeing, and there were no signs of tunneling. Desperate, he wrote in his adventurer's diary, "It may have passed through the door."

Since this report by the adventurer, there have been many similar reports of attacks by Thons. However, because these stories are too unbelievable, they are not recorded in official reports. They remain mere rumors.

It seems it will take quite some time for a brave adventurer to accurately report on their ecology.

Y Yeti

yeti

The ecology of yetis has been well-documented and can be found in detailed descriptions at the adventurer training school library. They have a large body, comparable to giants in size and strength. Their entire body, except for part of their face, fingers, and soles of their feet, is covered in white fur. Their skin is thin, and even a sword wielded by an adventurer can penetrate it. It has been confirmed that they possess intelligence, though at a low level. They cannot read or use many words for conversation. They often travel in groups of 10 to 20, but do not hunt in groups; they mostly act alone when seeking food.

Undead, Thon, Yeti

223


## Page 226

yeti

barrow wight

yuk / Hiro

vampire lord

giant ant

zombie

yuk / Hiro


## Page 227

Yetti are originally creatures that dwell in unexplored high peaks, but some have been wandering in the dungeons at the request of Yendor. They have excellent cold resistance, so attacks based on cooling will not work on them.

The main weapon of the yeti is its claws and teeth. They swing their arms with brute force, so it's important to gauge the opponent's movements to strike effectively. Due to their large size, there are many parts of their body that can be eaten. When hungry, they might become unexpected allies.

Finally, the text concludes, "A group of them would be a formidable opponent, but as individuals, even a newly graduated adventurer could match them or better."

Z Zombie

kobold zombie, gnome～, orc～,
elf～, human～, ettin～, giant～

A zombie (zombie) is a corpse given false life by Yendor's magic. There is no particular causal relationship between race and becoming a zombie. In fact, it has been confirmed that humans, kobolds, orcs, gnomes, giants, and even elves can become zombies.

They have no thoughts. They cannot see, hear, or feel. Their actions are almost reflexive, and they never attack adventurers or pick up items on their own initiative. They are living corpses.

Zombies are not undead. Their weakness is their head. Although they lack thought, if the brain is crushed, the obsession is lost and the zombie becomes unable to act.

Their attacks are primarily with their claws. While zombies themselves are not strong opponents, they can deal unexpected damage if you are not careful. New adventurers should be especially cautious.

It's best not to think about eating the rotting bodies of zombies. It can be dangerous and involve risks to your life.

a Insects

giant ant, soldier ant, fire ant,
giant beetle, killer bee, queen bee

The insects in Yendor's dungeon are cruel and ferocious. Enhanced by Yendor's magic, they are far more powerful than their counterparts on the surface. The jaws of ants are large, and the stingers of bees are much sharper. A bite from a golden beetle can tear through skin and muscle.

Zombie. Insects

225


## Page 228

Ants among them are those that inflict pain on adventurers with heat and flames when bitten, becoming a more dangerous existence than generally thought. The training manuals at the adventurer's training facility also state, "Do not underestimate insects. In the early stages of adventure, they will likely be the most formidable enemies."

Their danger lies in their tendency to act in groups. Like insect monsters, ants often hunt in groups, frequently attacking adventurers as a group. If an adventurer is struggling to defeat a single ant, they may find themselves with no escape route, completely surrounded and torn apart. Corpses ravaged by ants can be found scattered throughout the dungeon.

In this way, insects are a dangerous presence for adventurers, but occasionally bring about tremendous good fortune. When encountering large numbers of bees, one must not retreat. Several reports confirm that they can bestow powers beyond imagination upon victory.

b Liquid Creatures

acid blob, quivering blob, gelatinous cube

These mysterious beings are covered entirely in liquid or foam. They are born through the magic of Yendor and can only survive within the dungeon. Their shapes vary, sometimes forming small spherical blocks or cubes. Generally, they are smaller than humans, but there are rare instances of individuals larger than humans, surprising adventurers. Their eyes and ears are mostly black, emitting a smell akin to rotting fish.

Their attacks are carried out using parts of their bodies. Some creatures corrode swords and armor with acid foam, dissolving adventurers' bodies, while others can tear through opponents' bodies with a touch. Occasionally, they paralyze their targets, leaving them unable to act. While wounds themselves are rarely fatal, the unpleasant sensation remains. During combat, one can be entangled by their sticky bodies, even if successfully defeated, the foul odor persists. To completely eliminate them, one must wash their body with clean water for at least three days.

Adventurers have also devised ways to combat their foul odor, resulting in entire books dedicated to the subject. The efforts of predecessors are detailed in the "Several Strategies for Maintaining Cleanliness in the Dungeon" found at the adventurer's training facility.

226

MONSTERS—Monsters Roaming the Dungeons


## Page 229

<<<SOURCE
c Cockatrice

cockatrice

In some regions, it is also called basilisk or basilicock.

A strange monster with the body of a snake, the head and feathers of a male bird, and legs. It is larger than a human but does not grow as large as a dragon. While emitting a terrifying scream that even makes devils tremble, it flies through the air. It is said that its appearance is even more bizarre than that of a snake flying through the air.

Originally, it lived far away from the dungeons in deserts. However, it moved to dwell in response to Yendor's summoning. Details about its true form are not well known. It is said that snakes will flee upon hearing the cockatrice's (cockatrice) call, but no one has ever witnessed this. This is because if one were present at the scene, they would not survive.

The cockatrice's greatest weapon seems to be its body. Just touching the dark brown scales can turn adventurers into stone. Even if an adventurer manages to strike the cockatrice's body successfully, it is said that magic power flows through the weapon and turns their body to stone. Methods to defeat the cockatrice have been researched, but no official tactics have been officially published yet. Magic is said to be effective, but the truth of this claim is unknown.

Even if extremely hungry, it is better not to eat the carcass of a cockatrice. The cockatrice's magic remains in the corpse. The outcome is easy to imagine.

d Dogs and Dog-like Monsters

dog, little dog, large dog, jackal, were-jackal, warg, wolf, were-wolf, winter wolf, hell hound, pup

Canines are the closest creatures to adventurers. Many live closely with humans as pets, hunting dogs, or guard dogs on land. In the dungeons as well, they are similar. Dogs are trained in breeding facilities to guide adventurers into the dungeons. They sense the location of monsters by sound and attack together with their master. Using a faint scent that adventurers cannot detect, they judge whether a treasure is cursed and never touch it if it is. From the moment they enter the dungeon, dogs act alongside adventurers and fight by their side. They are the most trusted and reliable allies. Please cherish them.

Canine monsters basically use attacks based on fangs and claws. For small animals, it is just minor injuries, but for monsters, significant damage can be inflicted. Hell hounds from

liquid creatures. cockatrice. dogs and dog-like monsters

227
SOURCE
>>>


## Page 230

gelatinous cube

cockatrice

Yuk / Hilro


## Page 231

Guarded by a legendary hound, it is said that they attack not only with their fangs but also with a breath of heat that can melt iron, and without proper equipment, one can be defeated quickly.

Moreover, some monsters may cause injuries with their fangs as well as possess the adventurer themselves. When possessed, the adventurer cannot take normal actions and falls into a dangerous state. In the dungeons, there are corpses that cannot be determined as human or animal, but these are undoubtedly the result of possession. The monsters that cause possession often have the form of a half-human, half-beast, so as the training manual at the adventurer's training facility states, one should take appropriate measures when encountering such creatures.

It is also said that one should never eat the corpse of a humanoid even if they are starving. It is believed that the magic power of a humanoid does not disappear even after death.

O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O


## Page 232

Now, one of the spherical creatures appears to be just a white ball. The information about it is less than that of the eyeball. Apparently, it is quite a dangerous existence, and adventurers who fought it have suffered severe frostbite. One adventurer left behind the word 'explosion' just before dying, but its meaning remains unclear.

Cat Family Animals

kitten, housecat, large cat, jaguar, tiger

Cat family animals, like dog family animals, can become a powerful ally to adventurers. Unlike dogs, cats cannot be trained at a kennel. However, from the moment they are on the surface, the nature of cats is close to monsters, and they have the ability to instinctively determine whether items are cursed. Cats brought from the surface will not approach cursed items, so adventurers can judge what kind of item it is based on the cat's attitude. Moreover, contrary to the belief that cats are selfish and do not fight alongside their owners, they never do so. However, if the owner feels gratitude and affection towards them, they will fight monsters alongside their owner.

The weapons of cat family animals are fangs and claws. Rather, that's all they have. They may not be powerful as weapons, but they are well-versed in their use and can sometimes inflict significant injuries. For inexperienced adventurers, this should not be taken lightly.

However, as experience accumulates, cat family monsters cease to be formidable opponents. The lack of detailed descriptions of cat family animals in adventurer training schools indicates the threat level posed by cat family monsters to adventurers.

Gremlin

gremlin

A sub-species of goblins. They are generally said to be shorter than humans. It is commonly believed that they have the ability to fly, and sightings of them flying on the ground have been reported. However, the gremlins in Yendor's dungeon do not seem to possess flight capabilities. It is unclear whether they were transformed by Yendor's magic or if they simply do not feel like flying in the narrow dungeon.

The weapons of gremlins are fangs and claws. While the fangs are not particularly impressive, the claws can leave minor injuries depending on how they scratch. At times, they can steal special abilities from adventurers' bodies, so caution is advised. One adventurer reported that a special ability they had obtained by eating another monster disappeared after fighting a gremlin. There are also many reports of other abilities being stolen. Outside the dungeon, clean dishes and small objects would disappear if one were to momentarily look away. 

230

MONSTERS – Monsters Roaming the Dungeons


## Page 233

This is a common occurrence. However, I have never heard of taking away the abilities of a creature. Perhaps it is due to Yendor's magic, a newly added ability.

It is a helpful beast that cooperates with humans on the surface, but it often attacks viciously in the dungeon. Caution is needed.

Subterranean Dwellers

hobbit, bugbear, dwarf, lord, king

Dwarves (dwarf) are underground inhabitants that become troublesome creatures for adventurers.

Dwarves are a race with a slightly smaller build than humans. They move slowly, but they make up for it with more than enough strength. Their bodies are robust, and they live long lives, typically reaching around 200 years old. They are renowned for their excavation abilities and for digging extensive networks of tunnels to form underground cities. According to one account, Yendor's dungeon was also built by his subordinate dwarves, but this is uncertain. In any case, it is a fact that they have settled in the dungeon and attack from secret passages unknown to adventurers.

They are excellent warriors, attacking adventurers with swords, axes, and hammers. Due to the well-developed muscles they use for combat, they can inflict rather serious wounds if an adventurer does not properly parry their attacks. They will become formidable foes for adventurers who have little experience in the dungeon. The textbook at the adventurer training school states, "You are considered a true adventurer if you can easily defeat them."

Dwarves form clans similar to those of the gnomes, thus having clear ranks and being required to follow the commands of superiors. Dwarven Lords (dwarf lord) rank high in dwarven society, overseeing several clans. And Dwarven Kings (dwarf king) unite these clans, ruling over them as their monarch. A Dwarven King possesses higher abilities than a Dwarven Lord, and even experienced adventurers may struggle with him.

Hobbits (hobbit) are a race akin to dwarves. They never grow taller than a human's shoulder, with an average height below the waist. Their strength is small and their attack capability weak.

Carnivorous mammal. Gremlin. Underground dweller

231


## Page 234

gremlin

tiger

jelly

dwarf

tengu


## Page 235

Mysterious Creatures

manes, homunculus, lemure, imp, quasit, tengu

Many of them are summoned by Yendor to make the dungeon more solid, rather than being creatures created by Yendor himself. Appearing out of nowhere, they take up residence in the dungeon as if they were lodgers. In that sense, they resemble vampires, but unlike vampires who live together in a family and maintain close contact, they act individually, usually no more than two or three at a time, and rarely communicate with each other.

However, among them, only homunculi are produced from Yendor's magic. They are pseudo-humans born from magic.

Reports about them are scarce, and there are no official reports on their individual qualities. The only information available comes from adventurers' rumors. Indeed, these rumors are a compilation of several stories and are related to life and death, so they have some credibility. However, rumors are still just rumors, and the truth is not clear.

For example, there is a creature with an abnormally high nose that can move instantaneously and launch attacks that change form. Additionally, eating the corpse of this creature grants the eater the ability to move instantaneously. This is something that defies common sense, and the reports about this creature are quite suspicious. However, there are rare instances of adventurers possessing the ability to move instantaneously. Although none of them speak of how they acquired this ability, it is certain that they gained it after descending into the dungeon. It cannot be said that these are entirely rumors.

In any case, the truth is unknown about anything. To know their true abilities, one must fight them as an adventurer.

Jelly-like Creatures

blue jelly, spotted jelly, ochre jelly

Creatures produced by Yendor's magic. While sizes vary, larger individuals are more common compared to humans. They have bodies that shimmer and undulate, and their shapes are not fixed. They lack eyes, noses, and mouths. It is even unclear whether they possess senses. Their origin is also unknown, but it is believed that they are formed by melting several adventurers' corpses and fusing them. Were they created to clean the dungeon?

Their attacks are retaliatory, responding to the opponent's attacks. When an adventurer wields a sword,


## Page 236

When they are stabbed with a spear, they throw a part of their body like a knife. The body that is thrown contains acid and cold, and if it pierces an adventurer's body, it can inflict considerable wounds.

Some individuals use their main body for attacks. According to reports, a gelatinous, brownish body engulfs adventurers like a hug. The monster has powerful digestive juices, so even seasoned adventurers might find themselves in mortal danger if they are caught by it.

It is said that from an adventurer's perspective, they seem to be standing still, but once attacked, they are quite formidable. Adventurer training manuals also note at the end of their descriptions, "Since their true nature is unknown, do not let your guard down."

k Kobold

kobold, large~, ~lord, ~shaman

Small people clad in shabby clothes. They are light on their feet and can appear anywhere in the dungeon. While kobolds are not inherently aggressive, if you insult them, they will show their anger and attack. Kobolds within the dungeon are under the control of magic users, so they will immediately challenge any humans they encounter.

Kobolds are weak enough to be defeated by newcomers to the dungeon. However, there are some tougher kobolds such as kobold lords (kobold lord) and kobold shamans (kobold shaman).

According to adventurers, kobold shamans' magic is apparently minor spells that cause little to no injury...

l Leprechaun

leprechaun

A mischievous sprite, thought to be a member of the fairy family. Many adventurers have lost all their money to leprechauns.

Leprechauns move swiftly and possess teleportation abilities, making it difficult for adventurers to catch them. To defeat them, it is best to attack with ranged weapons or to strike while they are out of sight.

Additionally, leprechauns often sleep, so it might be better to leave them undisturbed if possible.

234

MONSTERS—Monsters wandering the dungeon


## Page 237

Mimic

small mimic, large mimic, giant mimic

A monster that can transform into various items and doors, and whose true form is still not fully known. Some say it is an amorphous creature, while others claim it is a four-legged beast covered in scales. They use their special ability to transform into inanimate objects, waiting for foolish victims.

If you enter combat with a mimic, those who have gained much experience in the dungeon can easily deal with mimics. However, if you are still new to the dungeon, it would be wiser to flee. While dealing with small mimics (small mimic) might still be manageable, facing large mimics (large mimic) or giant mimics (giant mimic) could leave you unable to escape from combat.

For those who have just begun exploring, it is important to distinguish between items and mimics at shops.

Nymph

wood nymph, water nymph, mountain nymph

They are said to be fairies in the form of beautiful women.

Several types of nymphs have been confirmed within the dungeon, including mountain nymphs (mountain nymph) living in mountains and rivers, water nymphs (water nymph), and wood nymphs (wood nymph) residing in forests.

The nymphs use their unparalleled beauty as a weapon, causing adventurers lured by them to lose the will to fight and submit to their whims. Although adventurers may lose the will to fight, nymphs do not intend to harm the adventurers. Instead, out of mischief or pity, nymphs sometimes steal large quantities of items from entranced adventurers.

Moreover, nymphs possess teleportation abilities, so even if an adventurer searches the dungeon for stolen items, they will move around instantaneously, mocking the adventurer.

One adventurer has said that a single nymph is more terrifying than a tough monster. This is because, unlike ordinary monsters, one can avoid them using items, but if deceived by a nymph, one would have to explore the dungeon naked without a sword or armor.

Cobold, Leprechaun, Mimic, Nymph

235


## Page 238

leprechaun

nymph

orc

piercer

mimic


## Page 239

Goblins, Hob Goblins, Uruk-hai, Orcs, Hill Orcs, Mordor Orcs, Shaman, Captain

Goblins (goblin) and Hobgoblins (hobgoblin) are of the same kind as their names suggest. They are small evil spirits, much smaller than adult humans. They prefer dark places and their dark red eyes, accustomed to the darkness, are very effective in the dungeons where sunlight never shines.

When comparing goblins and hobgoblins, the latter are slightly stronger and tend to appear in groups. When you see a hobgoblin, it's wise to be on guard that there may be more of them around.

Among the monsters inhabiting the dungeons, those of the orc (orc) type are among the most numerous kinds.

The backs of orcs are almost the same as those of humans, though they are said to have faces resembling pigs and are very ugly. Orcs prefer darkness, and their eyes, which glow red, like those of goblins, can spot enemies in any darkness.

For adventurers, a single orc is not a formidable opponent, but they often attack in groups, making things quite difficult. Among them, the Uruk-hai (Uruk-hai) are particularly dangerous, as they shoot poisoned arrows at adventurers in groups.

Rock Piercer, Iron Piercer

The rock-dwelling monsters lurking in the dungeon ceilings are called rock piercers (rock piercer) and iron piercers (iron piercer), divided into two types.

Over time, living in the dark dungeons, rock piercers have lost their eyes and limbs, and consist of a huge body with a mouth full of sharp fangs and a torso resembling a layered armor. They use their powerful jaws and fangs to drill holes in the ceiling and then wait with their heads down for prey to pass by.

Rock piercers that suddenly fall from above and attack are somewhat troublesome opponents. They hide in the ceiling, and their outer skin is tough, while attacks with their fangs are powerful. However, rock piercers also have weaknesses. Their body structure makes them unsuitable for movement on the ground, and they move slowly.

Goblins, Orcs, Rock Piercer

237


## Page 240

If you must engage them in combat, the hit-and-run tactic or ranged attacks would be effective.

q Giant Beasts

rothe, mumakil, leocrotta, wumpus,
titanothere, baluchitherium

Long-extinct beasts of ancient times, or those that appear in old legends, have been resurrected in the dungeons of Yendor by evil magic.

Their attacks involve biting with sharp fangs, tearing with sharp claws or horns, or using their overwhelming strength to attack adventurers. Despite their large size, they are not slow-moving and can be formidable monsters for adventurers.

Among them, Baluchitherium (baluchitherium), the largest terrestrial mammal of all time, belongs to the family of rhinos and can reach a length of 5.5 meters. When faced with the resurrected ancient creature Baluchitherium, even the bravest adventurer might wonder how to attack it.

However, these giant beasts also have weaknesses, particularly their low resistance to magic. For example, you could consider putting them to sleep with a sleep spell before attacking.

r

Mice
Rock Mole

sewer rat, giant rat, rabid rat, rat were,
rock mole

A race that has lived longer than humans—mice's adaptability to their natural environment is remarkable. In the Dungeons of Yendor, where a human might die within half a day, mice demonstrate their incredible reproductive power and vitality, living as if it were normal.

Most mice are not dangerous, and you can easily kill them if they attack. However, you should be careful with rabid rats (rabid rat). They carry a terrible pathogen, and if you get injured by one, there is a risk of being poisoned.

Additionally, there is a werewolf-like creature called a ratwere (rat were). They can transform from human to mouse and, if they feel threatened, can summon their small mouse companions. The most terrifying aspect is that if an adventurer is bitten by a ratwere and develops a fever, they will tragically turn into a ratwere themselves.

The appearance of the rock mole (rock mole) is literally bizarre. 

238

MONSTERS—Monsters Roaming the Dungeons


## Page 241

It appears as if they are rocks. There are few objects that can hinder the movement of rock moles that can pierce even hard rock, so they can move around freely throughout the dungeon.

It is not easy to defeat rock moles with their tough skin, but experienced adventurers can take advantage of their sluggish movements and easily defeat them.

S Spider, Scorpion

Representative spiders found in the dungeon are two types: one is the cave spider (cave spider), and the other is the vicious giant spider (giant spider).

Cave spiders are predatory spiders that do not build nests and hunt by ambushing their prey. Their attack consists solely of biting their target with their fangs.

Giant spiders are larger than cave spiders, and their fangs contain a terrible venom. When this venom enters the body, it weakens the victim's strength, leaving them unable to fight at full capacity, and they become prey for the giant spiders.

In most cases, giant spiders wait in their nests for prey, and in the center of their nest, various items are placed to lure victims, such as humans. When an adventurer tries to pick up an item and gets caught in the spider's nest, the giant spiders approach the foolish victim while dripping poison.

The tail of a scorpion contains a well-known potent venom. Although the type of venom differs, like the giant spider's venom, it has the effect of lowering the enemy's strength. It is crucial to quickly resolve a battle against a scorpion and avoid attacks from its venom.

T Lurker Above, Trapper

Lurkers above, also known as lurkers above (lurker above), hang from the ceiling of the dungeon and wait for adventurers to pass by. When an adventurer arrives, the lurker spreads its wings, resembling bat wings, and descends silently vertically, opening its huge and flexible mouth to swallow the adventurer whole.

If an adventurer is swallowed by a lurker, they must find a way to escape immediately. Otherwise, they will be slowly dissolved by the lurker's powerful stomach acid.

Giants, mice, rock moles, spiders, scorpions, lurkers above

239


## Page 242

baluchitherium

trapper


## Page 243

The same monsters known as Trappers are also creatures that attempt to swallow their enemies whole and digest them. However, in the case of Trappers, their main body hides underground, and they attack by sensing the vibrations of approaching prey.

It is said that Luca and Trappers were originally the same kind of creature, but over time, as they adapted to life in the dungeon, they diverged into different species.

### Unicorn

White unicorn, gray unicorn, black unicorn

A one-horned beast in the form of a beautiful white horse with flowing long hair.

Unicorns detest dirty humans and rarely show themselves before humans, let alone approach to interact. However, unicorns trust pure maidens and have been known to allow riders on their backs.

Their movements are swift like a gust of wind, making it impossible for ordinary humans to catch up. Their rear hooves are also a formidable weapon; inexperienced adventurers can be critically injured with a single strike.

Unicorns have a horn on their head, and the spiral-shaped sharp horn contains magical power, which is said to bring various good fortune to its owner. One adventurer reported that his blind eyes were healed, while another reported that poison water turned into plain water.

In the dungeon, besides the well-known White Unicorn, there are also Gray Unicorns (gray unicorn) and Black Unicorns (black unicorn). They are respectively the holy beasts of Lawful (good), Neutral (neutral), and Chaotic (evil). According to legend, killing a unicorn of one's own alignment brings misfortune.

---

### Fog Cloud, Dust Vortex, Energy Vortex, Ice Vortex, Steam Vortex, Fire Vortex

**Fog Cloud (fog cloud)** is a monster that attempts to suffocate enemies by surrounding them with fog. However, Fog Clouds move slowly, and they can be easily defeated unless the enemy is severely injured.

The strange vortex monster, Vortex, has several types due to its nature.

Firstly, there is the Dust Vortex (dust vortex), whose swirling wind contains countless particles of dust. When an adventurer is caught in its wind, they become temporarily blind.

Unicorn, Fog Cloud, Vortex

241


## Page 244

The energy vortex (energy vortex) is a whirlwind that emits lightning bolts, and anyone caught in the wind will be struck by lightning attacks. The ice vortex has chunks of ice swirling in the wind, and performs attacks with extremely low temperatures. Next are the steam vortex and fire vortex, where those enveloped by them will be attacked by scalding steam and blazing flames, respectively.

Adventurers caught in a vortex not only suffer severe injuries, but there is also a risk of valuable items being destroyed. The lightning from the energy vortex often destroys staves and rings, while the cold from the ice vortex turns potions to ice. The steam and fire from the steam and fire vortices can ignite scrolls and magic books, and even cause potions to boil and explode.

If you encounter them, it would be best to avoid combat, or if you must fight, hide the types of items that the vortex can destroy before engaging in battle.

Worms

baby long worm, baby purple worm, long worm, purple worm

Worms are giant ring-shaped animals. They move through the interior of the dungeon by writhing their massive bodies and immediately attack any living beings they encounter.

In the dungeon, two types of worms have been confirmed.

One is the long worm (long worm), whose copper-colored body is incredibly long. The nerve center of the long worm is in its head, and no matter how much the body is cut, it will continue to attack as long as the head is not crushed. Additionally, the long worm's mouth contains sharp and sturdy fangs that can be crafted into excellent weapons.

The other is the purple worm (purple worm), which, as its name suggests, has a eerie purple body. Although its body length is not as long as the long worm's, its offensive power surpasses that of the long worm. When a purple worm encounters an enemy, it attacks with its fangs and then opens its enormous mouth to swallow the opponent and dissolve it inside its body.

Baby long worms and baby purple worms have also been confirmed, but they are reported to pose no such danger as adult worms.

242

MONSTERS—Monsters wandering the dungeon


## Page 245

Grid Bug, Xan

Grid bug (grid bug) is a bug that feeds on electricity, rarely taking any damage but capable of attacking with electric shocks. It appears in shallow layers and it has been reported that there is no monster as easy to defeat as the grid bug for adventurers.

Xan (xan) is an insect with jaws that can open to reveal large pincers. They can fly swiftly through the air by flapping their wings, and their bodies are covered with a thick exoskeleton, making it difficult to inflict fatal injuries upon them.

If you enter combat with a Xan, it would be better to use an item's power to float in the air. This is because they constantly hover low to the ground, trying to tear at the legs of humans with their fangs, and showing their vulnerable lower abdomen to the enemy would be disadvantageous.

Y Yellow Light

Yellow light

If you see a spherical object floating in the darkness of the dungeon's air and emitting yellow light, it is undoubtedly a Yellow Light (yellow light).

It is said that the Yellow Light is a semi-biological creation made by the magician Yendor to torment adventurers. They wander inside the dungeon day and night, approaching adventurers who have come seeking treasures.

If you find a Yellow Light, attacking it with a sword is a very dangerous choice. This is because the only method of attack for a Yellow Light is to explode and injure the enemy. Moreover, when a Yellow Light explodes, it is accompanied by intense flash. As a result, adventurers will suffer severe injuries and become blind. Even seasoned adventurers could easily be defeated if discovered in this state by other monsters.

To deal with a Yellow Light, it would be best to use ranged weapons while becoming transparent and maintaining distance, or to blind yourself and attack directly.

Becoming blind in a dangerous dungeon is akin to inviting death, so it is not recommended to engage in battle with a Yellow Light without any preparation.

Worms, Bugs, Yellow Light

243


## Page 246

iron golem

yellow light

worm

dust vortex

xan


## Page 247

Beast. Golem

zruty

A giant creature inhabiting the open fields at the foot of the Tatras mountains.

Only rumors exist about it, either that it is a savage humanoid resembling apes, or a beast with fangs so fearsome that they can fell a bull with one strike.

However, based on speculation from these rumors and adventurers' testimonies, it is certain that the monster has sharp claws and huge fangs. It is also somewhat cumbersome, but moves fairly quickly.

• Golem

straw golem, rope golem, leather golem, wood golem, flesh golem, clay golem, stone golem, iron golem

Golems are not beings born in nature, fairy realms, or the netherworld. They are pseudo-lifeforms without souls, brought forth by some mysterious magical power.

Golems created by magic are classified according to their material. There are straw golems made from straw, rope golems made from rope, leather golems made from leather, wood golems made from wood, flesh golems assembled from corpses, clay golems formed from lumps of clay, stone golems constructed from stones, and iron golems made from iron.

Golems faithfully and accurately follow the commands of the one who created them. The effectiveness of these commands lasts until the golem's body is completely shattered or the caster changes the command.

Some golems possess special abilities. For example, a rope golem can entangle its body's rope around an enemy, immobilizing them. A stone golem can blow toxic mist from its mouth towards its opponent.

The attacks of golems, which lack defensive movements, are terrifying due to their strength. Adventurers might consider fleeing if they believe they cannot defeat them.

Beast. Golem

245


## Page 248

<<<SOURCE
Giant Eel, Electric Eel, Kraken

There are giant eels living deep in the dungeon. While ordinary edible eels rarely harm humans, giant eels that live in the dungeon can easily take the lives of adventurers.

The giant eel attacks adventurers with its dreaded fangs, and if it is an electric eel, it can also send currents strong enough to kill a water buffalo through its enemies. However, what is most terrifying about the giant eel's attack is the way it wraps its long and thick body around adventurers and drags them underwater.

There is a legendary monster called the kraken along the coast of Norway.

The kraken is so enormous that its adult form is not well known. According to legend, its back resembles a small island floating on the waves, with shells and sometimes even trees growing there. It can extend tentacles longer than ship masts from the water, which are neither arms nor horns.

Because of its massive size, the kraken moves slowly, so attacking quickly is an effective strategy. However, if caught by the kraken's tentacles, you may be dragged deep into the water, so great care must be taken during combat. If you are pulled underwater, there is no hope for the adventurers, as the water is their most advantageous battlefield.

@

Humanoids

Humans, Elves, Were-creatures, Medusa, The Wizard

Many humanoid monsters inhabit the dungeon.

Various races such as wer-creatures that transform into animals, elves, and soldiers wait for adventurers at the bottom of the dungeon.

Among these terrifying monsters, Medusa is also a humanoid. Her hair consists of venomous snakes, and even if you manage to exploit Medusa's weakness, she will bite you with her snakes.

Medusa's attack against her enemy is simply to direct her glowing red eyes at them. However, the effect is tremendous, and anyone who meets her evil gaze turns into a stone statue. However, such a Medusa can be easily killed with a certain shield, as the Greek

246

MONSTERS—Monsters Roaming the Dungeon
SOURCE
>>>


## Page 249

As when the mythic hero Perseus slew Medusa.

Another person must be mentioned as a human form. This is the great and evil mad wizard who rules this dungeon, the Wizard of Yendor.

It is unknown why he created such a vast dungeon, save that the name of the wizard Yendor is widely known in tandem with the fearsome dungeon.

All about the attacks of the wizard Yendor are shrouded in mystery, for no one has survived a battle with him...

---

Demons

water demon, incubus, succubus, and more...

Most adventurers will never see most of the demons. Apart from the relatively shallow levels where water demons and incubi appear, the truly vicious monsters that could be called demons reside deep within the dungeon. It is just a rumor, but it is said that the demons live in a deep abyss called the Inferno at the bottom of the dungeon.

The attacks of these monsters are powerful, and they are known to use a variety of magical attacks in addition to weapons.

If you ever encounter a powerful monster called a demon, you will have to choose one of two paths unless you are exceptionally strong. That is, either flee using any means available, or invoke the name of the gods and ascend to heaven.

---

Ghosts

ghost

After a person dies and becomes a skeleton, their soul may remain, wandering the earth as a ghost. There are ghosts in Yendor's underground labyrinth, many of which are the forms of adventurers who died during their quest.

According to gathered information, ghosts often stay still on their own skeletons or items. They move slowly, but being ethereal makes them hard to damage, and they can pass through walls and corridors, which can be troublesome for inexperienced adventurers.

However, the attacks of the ghosts are to gradually suck away the life force of adventurers by touching them, so it is unlikely that you will die instantly in combat. If you want to avoid combat,

turtle, kraken, humanoid, demigod, ghost

247


## Page 250

elves

succubus

kraken


## Page 251

It might be best to escape by using speed to run from that floor.

If you manage to defeat a ghost, what brings the most joy is the various items collected by the adventurers who turned into ghosts. However, it's worth considering not to use items out of sheer happiness. This is because most of the items in the deceased's possession are cursed.

Be sure to take care so that you don't turn into a mummy while collecting mummies.

Eel, Kraken, Humanoid, Demi-human, Ghost

249


## Page 252

Preface by Author Sandras Forn

Information

Very few return from Yendor's dungeon alive. Those who returned with Yendor's amulet can be counted on one hand. They have become heroes, or even more than that, 'existences'—though it is uncertain if they actually obtained Yendor's amulet.

However, those who did not obtain Yendor's amulet but searched deep into the dungeon and returned also exist. Dioles is one of them. When he came out of Yendor's dungeon, his hair, which was originally light chestnut, had turned white, and his once robust body had shrunk and aged like that of an old man.

I asked him many questions about Yendor's dungeon. However, that dungeon had infected not only his body but also his mind. Dioles' answers were fragmentary and vague, sometimes seeming to make no sense at all. He would suddenly answer questions from two hours ago, or simply mutter to himself without answering anything.

By combining such stories with rumors that have been circulating, I managed to compile this information as a guide for those who venture into Yendor's dungeon. However, whether this information is correct or incorrect, I cannot judge.

I hope you, who venture into Yendor's dungeon, will verify the truth of these pieces of information yourself.

This book is dedicated to the beloved mad warriors—

250

INFORMATION—For those who wish to conquer the dungeon


## Page 253

Encounter with Diolus the Barbarian

He lived near the slums, beneath a bridge. His home was a shack that barely deserved to be called a house. For a warrior of his prowess, a grand mansion would have been built to honor him. However, perhaps his very spirit desired to reside in such a place.

This is where I am about to visit, the dwelling of Diolus the Barbarian.

Until a few years ago, he was renowned as a Barbarian. He boasted of his massive frame and claimed that he could cleave anything with the greatsword in his hand.

And in an attempt to showcase his might to all, he foolishly challenged the dungeons of Yendor.

Though he failed to obtain the protection against Yendor, Diolus did survive the dungeons.

Along with many treasures.

Had it been only this fact, he would have been hailed as a hero.

But now, Diolus is far removed from any such glory.

When he emerged from that dungeon, the muscles that had been full of steel had withered away.

The chestnut hair that had once been envied by many girls had turned into tattered white hair.

His eyes had lost their luster, colored by fear. The words that escaped his lips made no sense.

I, who am not a god, cannot know what terror befell him.

But one thing was certain.

Diolus's spirit had shattered in the dungeons of Yendor. Since then, he has been living in this shack, isolating himself from others, and surviving in the darkness. Occasionally, he would venture into town, selling the treasures obtained from the dungeons for a pittance.


## Page 254

He seemed to be using it for living expenses.

If one knew his former appearance, they would have been amazed at how different he had become. Now, Diores appeared almost like a living dead.

However, there was no doubt that he had delved deep into Yendor's dungeon. The knowledge he gained from his experiences held great significance for my research.

So, I stood before his door.

When I opened the door—though I skipped knocking because the door seemed about to collapse from the knock—I was greeted by a pungent odor that stung my eyes.

As light filtered through the doorway, two eyes glinted deep in the darkness, meeting mine.

Instantly, he moved. Into the corner of the room where a little darkness remained, avoiding the light.

And then, he threw things at me, uttering inarticulate growls as he desperately tried to escape into the darkness. It gave me a slight sense of despair; perhaps Diores could no longer engage in any form of social interaction.

Thus, our first meeting ended half in despair. After I left, he continued to throw things, scattering them around his dwelling, seemingly dreading even the light itself.

First Encounter, Initial Meeting

However, I did not give up and visited his home several more times afterward. Of course, I brought some gifts each time.

Initially fearful of me, Diores gradually opened up, and during periods of good mental health, we exchanged a few words.

He particularly enjoyed drinking 'Dwarf Wine'. Perhaps the intoxication helped to dissipate the fear that had shattered his heart.

That day, I brought 'Dwarf Wine' again. He was unusually


## Page 255

Became talkative and started talking about the dungeon of Yendor.

"The dungeon of Yendor is beyond description with words of terror. No, it was an amazing experience... but..."

When the subject turned to the dungeon, he would either become completely mute or extremely talkative. This time, because he became extremely talkative, I was able to obtain some important information.

First, I asked about the legendary weapons said to be sleeping in the dungeon of Yendor. The rumors of swords forged in ancient times always make our hearts race.

Diores struggled to find the right words to answer my question, scratching his white hair. In an attempt to coax out the words, he drank more alcohol. And the answer that came back from him was somewhat unclear.

Several mutterings of blasphemy against the gods leaked out, and only then did he squeeze out the words from the depths of his heart.

Exchange, First Meeting

253


## Page 256

"Longsword (long sword)... If you think your skill is worthy of praise, try immersing the longsword in the spring. The lady who resides in the spring will lend you great power if she acknowledges your skill."

"Spring... To immerse the cursed object in the spring... Yes, the water's power can cleanse the curse. However, there is considerable danger. Immersing it could turn scrolls to blank paper. You could even drink the water... Provided you are not afraid of nymphs or water demons..."

After repeating some nonsensical words, his eyes seemed to be lost in space, as if recalling something from deep within his heart.

Suddenly, light appeared in his eyes. As if something had taken control of him. Or perhaps, this was his true form.

His lazily open mouth tightened, and his eyes shone with a new vigor. He was no longer the Diores I had met earlier. It seemed like the expression of a warrior of old had returned.

"There are rare instances where you might find it in the corner of a weapon shop or general store. Probably sold by an adventurer desperate for money. My funds were insufficient to purchase it."

Taking a sip of the drink, he continued.

"You asked about enchanted weapons? If you truly desire an enchanted weapon, continue offering sacrifices to the temple of the god you hold dear. There may be divine favor."

I felt as if another Diores was speaking. His words flowed like a mighty river without hesitation, each one filled with dignity and grace. Perhaps the Diores respected as a warrior of old had returned. It was hard to tell if the man before me was the same one I had met for the first time.

Next, I asked about the existence of a temple in Yendor's dungeon. From various pieces of information, I had speculated that a temple existed, but I had no idea why it would be there. Now, Diores was talking about the

254

INFORMATIONS——To Overcome the Dungeon
SOURCE
>>>


## Page 257

There is a temple in the cave, he asserted.

"Indeed. But more of a altar than a temple. There are no temples with priests, but you have to go deep down. After all, obtaining Yendor's amulet is a religious ceremony."

Obtaining the amulet as a religious ceremony? What does that mean? However, Diores did not give me a chance to ask questions and continued talking to himself.

"Praying to the gods on the surface of the dungeon is the most important thing. By bringing the gods on your side, you can navigate through various difficulties that occur in the dungeon."

I asked about the method to bring the gods on my side. If I could bring the gods on my side, even that dungeon would be somewhat easier to move around in.

Exchange, First Meeting

255


## Page 258

"It is to offer sacrifices at the altar of the god you belong to. Continue offering the bodies of the monsters you slay. The larger and more powerful the sacrifice, the greater the回报 will be. When four-leaf clovers fall, it means the gods have accepted your offerings. By doing this, you can gain the favor of the gods. You can even communicate with them, and they might even bestow a legendary sword upon you. I did not receive such favor."

It seems that on Yendor, the power of the gods increases compared to our world. Only a handful of priests can communicate with the gods on the surface, and even they cannot receive gifts from the gods.

When he could not find the altar of the god he was offering sacrifices to, the question arose as to what he should do.

"Any god will do. First, find the altar. Just keep offering sacrifices to it. Of course, to the god you worship. If the power of the god you worship is strong, the altar will transform. For example, turning into Morrigan's altar,"

256

INFORMATIONS——To Overcome the Dungeon
SOURCE


## Page 259

I would like to show you the light when it shines. Truly moving was the time when that black light enveloped the altar...

In Yendor's dungeon, even struggles among the gods become intense. It is said that the distortion of time and space occurs within that dungeon due to Yendor's magic power. Such things might be related to his words.

...When my thoughts were wandering, Diolus let out an unbelievable statement.

"Sometimes it might be interesting to offer humans to the temple"

When he muttered those last words, madness was clearly reflected in his eyes. It seemed he had offered human corpses to the temple before. His expression was one of rapture.

And then he started spouting nonsensical words.

"The bouncing bridge... moat... floats. Only if the gods teach us the melody..."

"Become xorn... just become xorn..."

I realized that further questions would be futile. The day we started talking was over.

The next day, his mental state appeared to be good — or at least, that’s how it seemed.

He would sometimes shout meaningless words, but he mostly maintained a state of relative stability. During our conversation about divine blessings and curses, such words slipped out.

"Among cursed items, there were times when black flashes (black flash) or amber flashes (amber flash) appeared when placing something on the altar... Do you know what these mean? Black light means a curse, and amber light means a blessing. With this knowledge, you can safely navigate Yendor's dungeon."

Judging whether an item is cursed or not is important.

Exchange, first meeting

257


## Page 260

This can be considered the most crucial point in advancing through the demon's dungeon. This was something that became clear through my previous research. There have been quite a few adventurers who lost their lives by carelessly equipping items they obtained without knowing that they were under a strong curse.

"Just remember, pouring water on the altar is pointless. Water is blessed or cursed by the power of the god on the altar. If you pour water on an altar of a chaotic god like Molrigan, everything will turn into cursed water. The altars of gods of discipline work in the opposite way."

He also taught me how to make holy water. It is said that if you immerse a cursed object in holy water, it can be de-cursed.

These two pieces of information can be considered highly significant results. That day, I was satisfied with just these two answers. And the next day, when I visited his home—

"Recalling the cursed objects..."

He suddenly began answering my question from the previous day.

"When entering the dungeon, having a pet along is not only a friend but also a useful tool. Do you understand? Dogs and cats can judge whether something is cursed or not. Cursed items emit a scent that only they can detect. They won't step on cursed objects. Priests may rely on their holy powers, but it might just be their sense of smell."

Diores let a vulgar smile play at the corners of his mouth. My nape bristled with disgust, and chills ran down my spine.

He then downed a drink. The alcohol had smoothed his tongue and temporarily reformed his shattered mind.

Next, I asked him about scrolls. After several discussions, one statement stood out:

"I was once forced to wear leg irons and a ball and chain in the dungeon after reading three scrolls of punishment. I either read a scroll of remove curse or cast the remove curse spell to escape..."

258

INFORMATION—For Overcoming the Dungeon
SOURCE


## Page 261

I thought he could not have been familiar with magic, but I refrained from saying it outright. Here, I felt it would be better to avoid any objections that might spoil his mood—and perhaps even his memory.

Diores took a breath and tried to pour wine into his cup. However, only a few drops of liquid dripped from the bottle. He wrinkled his nose and, in an attempt to catch the last bit of wine at the bottom, turned the cup upside down.

"But there was one time when I turned into a monster that ate iron... I noticed that creatures like the Last Monster and Iron Golem really loved iron. I thought that if I turned into an Iron Golem, I would be able to eat iron."

Exchange, First Meeting

259


## Page 262

Dioles continued to mutter, perhaps recalling the taste of the iron ball he ate when he turned into an Iron Golem.

"There are also ways to summon such monsters using magic or scrolls, and then offer them the iron ball. In that dungeon, there should always be several escape methods even if you find yourself in a tight spot. Use your head. Those who are not clever cannot survive in that dungeon..."

Dioles suddenly slumped his shoulders. It seemed that a bittersweet memory had struck him. He took a long, deep sigh.

"Cannot survive..."

Dioles repeated those words several times. I sensed the limits of his mental strength and ended our conversation for the day.

Reflections on cursed items

A few days later, he continued his monologue as if pouring out his heart. The Dioles of recent times seem to be a completely different person from the one we first met.

However, understanding which question his words answered required considerable effort. For example, consider the following:

"If you obtain a cursed scroll of genocide, enter a small room and lock all the doors. Then, remove your weapons and take off all your armor. Read the scroll of genocide and try to kill the nurse. However, the cursed scroll of genocide will likely summon many nurses. Simply wait for time to pass. They will heal you..."

Dioles scratched his hair and buried his face in his hands. His eyes were completely devoid of light.

"Do not forget to remove your weapons and armor... When cursed armor, read the scroll that destroys the armor. The armor will shatter along with the curse."

He was explaining the effective use of items that seemed useless at first glance.

260

INFORMATIONS——Conquering the Dungeon
SOURCE


## Page 263

It seems so. Reading through my notes (surprisingly, he could read), he had cited examples of how using it in ways other than intended could be helpful.

No, he was simply recalling his experience and speaking it out. As evidence, there was no sense of will in his tone...

In moments like this, Diores reverts to being somewhat of a half-patient. However, even in such circumstances, he cannot forget about the dungeon...

I do not know what he saw in the dungeon. But, whatever it was that his eyes fell upon, it must have trapped him in such a terrible memory. As a researcher of the dungeon, it is an interesting subject, but I would not wish to experience something like that myself.

The Food Situation in the Dungeon

About a month had passed since I first visited Diores' home. His mental state was still relatively good. At this point, he would even greet me. Through our conversations, it seemed his mind was being reconstructed.

On this day, I asked Diores about the food situation in the dungeon. While some bring in a little food, it is impossible to carry all the provisions needed to traverse the dungeon, which extends to dozens of floors, in just a few days.


## Page 264

It is almost impossible.

However, this doubt was easily resolved by Diores' answer.

"Many of the monsters in the dungeon do not know that they can be eaten. There are also grocery stores and food scattered around. You can get enough nutrition and even feel full sometimes. Of course, you are often hungry, but it's not that bad. Just, there's nothing you can do about the taste."

As long as you don't fuss over the taste, the food situation in Yendor's dungeon isn't that bad. However, I still don't want to eat goblin or orc meat.

Furthermore, Diores provided some valuable information regarding the taste of monster meat.

"Some monsters with special abilities have their abilities transferred to you when you eat them... For example, after eating ants that can withstand fire, I no longer felt the heat of the fire. Such things happen. However, there are many that contain poison, and some become unrecognizable immediately after eating. Once you've eaten them, you won't forget, but being attacked by other monsters right after eating such things is the worst case scenario..."

I had heard similar stories. People who ate the meat of dimensional transcendence monsters like leprechauns or nymphs gained that dimensional transcendence power. However, since these stories often ended with the person losing control of the power and dying inside the wall, it was very difficult to determine whether they were legends or the truth.

According to his words, obtaining such abilities is not something that always happens, and it is quite dependent on luck. Additionally, the stronger the monster you defeat, the easier it is to obtain such abilities.

After that, Diores talked about many monsters' characteristics. Details about the characteristics of monsters are explained in my book, The Dungeon Exploration Book, Biology Edition. Please refer to that. Much of his talk was based on that.


## Page 265

According to the story, Diolus had even defeated dragons. There was nothing to prove his words, but it is probably true. He might have fought a young dragon.

Last Hour • His Death

A considerable amount of time had passed since I first visited his home.

On that day, I had nearly finished writing this book and went to Diolus to get it confirmed. However, what I saw at his house was his corpse.

He had been sorting out several treasures—perhaps obtained in Yendor’s dungeon—and had died on the bed. Beside him was a letter addressed to me.

The letter indicated that Diolus was aware of the abnormality in his mind. Furthermore, he knew that his life was running out, and thus, while his mind was still clear, he tried to convey as much information as possible to me.

He wished that by recording the various experiences he had in the dungeon through my writings, there would be fewer people who would fall into madness like him.

Therefore, this book, which was intended to circulate among a few people as part of my research, has now been made public.

To reiterate, the former Diolus was a strong warrior. Such madness exists in the dungeon that can turn a man into such a state. Those who cannot fight against this madness should not enter Yendor’s dungeon even if their goal is treasure.

It is a trial that requires more than one’s life as a price, and I hope you will understand the will of Diolus.

Last Hour • His Death

263


## Page 266

It is one of the religions. Islam is a religion based on the tenets of Islam. Islam is a religion based on the tenets of Islam.


## Page 267

Command List

■ Actions

Commands with a caret (^) require pressing the specified letter key while holding down the CTRL key.

Commands with a hash (#) require first typing # followed by the specified letter.

• Movement-related commands

>Go up to the upper level (when on a staircase)

<Go down to the lower level (when on a staircase)

.rRest

.cClose a door

.oOpen a door

.^Teleport if you have the ability

.#Jump to another location

• Commands to examine your possessions

.iDisplay all items

.lDisplay items of a specified type

.xDisplay list of known spells ('+' works the same)

.)Display equipped weapon

.[Display equipped armor

.=Display worn rings

."Display worn amulets

.(Display used tools

.$Count gold coins held

.§Display what kinds of things have been found so far

.^Inspect shops

Action commands

265


## Page 268

• Commands to Manipulate Items

A Remove all worn armor

d Drop all items

D Drop some items

P Put on amulet, ring

r Read scroll or spell book

R Remove amulet or ring

T Remove any one piece of armor you are wearing

w Pick up a weapon. Use "w-" to be unarmed

W Wear armor

u Pick up an item from the floor

#n Name an item you are holding

• Commands to Use Items

a Use a tool

e Eat food (or a monster corpse)

q Drink a potion of water

t Throw an object. Or shoot an arrow with a bow

z Strike with a wand. If it's a magic wand, its effect may occur

#d Soak an item you are holding

• Other Actions

^D Kick something (usually a door)

⊞ Carve a message into the floor

p Pay for items bought at a shop

s Search for secret doors or traps (usually requires several searches)

Z Cast a spell

: Show what is on the floor near you

#c Talk to something next to you.

#f Pry open a door with a key

266

List of Commands——Command List


## Page 269

# Loot the contents of a box below, or your backpack

# Use a monster's special ability

# Offer a sacrifice on an altar to the deity

# Pray to the deity for help

# Rub a lamp to summon a genie

# Sit down at the current location

# (If available) Expel an undying monster

# Disarm a trap

# Wipe your face

## Player Commands

? Open the help menu

/ Display the description of symbols shown

& Display the action description of commands

^a Repeat the last command executed

C Name individual monsters

D Set options

^p Redisplay the previous message (continuously executing this will show previous messages in sequence)

Q Quit the game

^r Redraw the screen if it is damaged

S Save and exit the game. You can resume from the saved location next time

V Show the version number of NETHACK

V Show the history of NETHACK

^-NETHACK Show the options used when compiling NETHACK

X Enter discovery mode (invulnerable mode). Once entered, you cannot return to normal mode.

@ On/Off option for the pickup command. Changes by pressing

! Exit to DOS shell. To return to the game, type 'exit'

Player Commands

267


## Page 270

And to my surprise, this book came into being (laughs).

To recall, it all began when I started searching for interesting free software games to write about for the Game Collection 30 that came out at the beginning of last year. All the games covered in this book were excellent, but NetHack particularly suited my feelings so well that the first time I played it, I found myself losing track of time, having passed an entire day and night.

Also, due to file size constraints, we had to abandon including NetHack with the Game Collection 30, but upon returning, the survey postcards showed that there was a relatively high demand for playing NetHack.

So, rather than just introducing NetHack in a single volume and putting it on a disk, it wouldn't be interesting enough or too trivial. Could we make it more interesting by incorporating various experimental elements... The result of such deliberation led to the creation of this book (laughs).

In a way, one co-author stopped communicating for a while, and when I placed an order for illustrations, the results were something entirely different. This unusually difficult and lengthy writing process from concept to execution took up to nearly a year, but it was quite enjoyable.

For this reason, I would greatly appreciate any feedback you might send. Your voices truly have power.

Now, how will I present myself in front of you all next time? Please look forward to it (surely it will be part 3 of the Game Collection 30, right? I'm not that straightforward of a person). 

268

Have you enjoyed your own hacking?—Afterword


## Page 271

Thought you had finished your own hacking?——Afterword

1993年·4·1 Rokishiro Tanekawa

Postscript

The version of NetHack included in this book's attached disk is 3.0 j.

However, at the very last moment of writing this book, it was announced that NetHack 3.1 had been released across the sea! Moreover, the port to PC-9801 turned out to be relatively easy, and it has already been released. Distribution through various BBS is proceeding smoothly.

There have been several changes——such as the increase in items——.

But, the authors have yet to fully grasp the entirety of NetHack 3.1. And, (well, no, that).

So, that's why.

Regarding the inclusion in this issue, please bear with us using NetHack 3.0 j (I've been saying "it's coming, it's coming" all along, but it hasn't appeared yet. Sigh). 

Have you enjoyed your own hacking?——afterword

269


## Page 272

page=272

SOURCE
>>>


## Page 273

Welcome back

Freesoft library Game Collection Extra
NetHack the RPG—with FMP & MAG loader—

Planned and Supervised by Rōshi Ryūsirō

Written by Rōshi Ryūsirō, Tomoyuki Suzuki, Shin Iki, and Shōichirō Itei

Front Cover CG and Back Cover CG by AROUND2

Illustrations in the Text by Seirō Gokō, Takahashi Yōko, Kunihiko Inoue, and Keiko Ishikawa

CG by Yōko Takahashi, Seirō Gokō, Takahashi Yōko, and Kunihiko Inoue

Music by KID and Ueno Sai (Fiction)

Special thanks to ...Kzoo, Guu, SAM, Shinsuke Koizumi, M. Stephenson


## Page 274

● Please send your comments and feedback about this book and the game to our service center in writing. However, please note that we may not be able to answer all content-related questions due to the nature of the game.

● If you believe there is a malfunction, please write in detail about your name, address, the type of computer you are using, how you operated it, and what happened before and after the issue occurred. Please also enclose a return envelope and send it to our service center in writing. We may not be able to respond to inquiries made by phone, so please understand this.

● The disk attached to this book does not contain the source code of NetHack due to storage limitations. If you wish to obtain the source code, please fill out the necessary information on the reader card attached to this book and return it to us. 

Free Software Library • Game Collection • Extra

NetHack the R. P. G.

Published July 14, 1993

Authors: Haska Wariyashiro, Iba Zoichiro, Suzuki Naoyuki,

    Araki Shin

    Suzuki Shin

Publisher: Kusa Yoshizou

Publisher's Office: Showa System Trading Co., Ltd.

    〒107 Tokyo, Chuo Ward, Akasaka 8-5-29 Checker Building

    TEL 03-3470-4941

Printer: Jokyosha Printing Co., Ltd. Printed in Japan

ISBN4-87966-322-0 C3055

The cover shows the price.

If you have a book with missing pages or lost pages, please send it to our sales office for replacement at no shipping cost.

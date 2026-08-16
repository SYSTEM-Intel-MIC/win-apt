"""Easter eggs for WinApt - apt moo and friends"""

def apt_moo(verbose=0):
    """The famous apt moo easter egg"""

    if verbose == 0:
        # Basic moo
        print("         (__)")
        print("         (oo)")
        print("   /------\\/")
    print("  / |    ||")
    print(" *  /\\---/\\")
    print("    ~~   ~~")
    print("....\"Have you mooed today?\"...")

    if verbose >= 1:
        print()
        print("        \"I sense evil within that cow.\"")

    if verbose >= 2:
        print()
        print("              \"Evil is everywhere.\"")
        print("                    \"Everywhere.\"")

    if verbose >= 3:
        print()
        print(" ________________________________")
        print("< Super Cow Powers activated!!!  >")
        print(" --------------------------------")
        print("        \\   ^__^")
        print("         \\  (oo)\\_______")
        print("            (__)\\       )\\/\\")
        print("                ||----w |")
        print("                ||     ||")

    if verbose >= 4:
        print()
        print("         (__)")
        print("         (oo)")
        print("  /-------\\/")
        print(" / |     ||")
        print("*  ||----||")
        print("   ^^    ^^")
        print("   \"I am the cow of the borg.\"")
        print("   \"You will be assimilated.\"")
        print("   \"Resistance is futile.\"")

    if verbose >= 5:
        print()
        print("   \"The cow says: Moooo!\"")
        print("   \"The duck says: Quack!\"")
        print("   \"The apt says: Have you mooed today?\"")
        print()
        print("   [System message: Maximum verbosity reached.]")
        print("   [The cow is now omniscient.]")
        print("   [All your base are belong to us.]")
        print()
        print("              (__)    (__)")
        print("              (oo)    (oo)")
        print("       /-------\\/  /-------\\/")
        print("      / |     ||  / |     ||")
        print("     *  ||----||  *  ||----||")
        print("        ^^    ^^     ^^    ^^")
        print("   \"We are the cows. Lower your shields.\"")
        print("   \"Your distinctiveness will be added to our own.\"")


def apt_get_moo(verbose=0):
    """apt-get moo - slightly different flavor"""
    if verbose == 0:
        print("         (__) ")
        print("         (oo) ")
        print("   /------\\/ ")
        print("  / |    ||   ")
        print(" *  /\\---/\\ ")
        print("    ~~   ~~   ")
        print("....\"Have you mooed today?\"...")
    else:
        apt_moo(verbose)


def apt_sl():
    """Steam Locomotive easter egg (like sl command)"""
    train = r"""
      ====        ________                ___________
  _D _|  |_______/        \\__I_I_____===__|_________|
   |(_)---  |   H\\________/ |   |        =|___ ___|      _________________
   /     |  |   H  |  |     |   |         ||_| |_||     _|                \\\_____A
  |      |  |   H  |__--------------------| [___] |   =|                        |
  | ________|___H__/__|_____/[][]~\\_______|       |   -|                        |
  |/ |   |-----------I_____I [][] []  D   |=======|____|________________________|_
__/ =| o |=-~~\\  /~~\\  /~~\\  /~~\\ ____Y___________|__|__________________________|_
 |/-=|___|=    ||    ||    ||    |_____/~\\___/          |___ ___ ___ ___ ___ ___|_
  \\_/      \\O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O/

    CHOO CHOO!  All packages aboard!
    """
    print(train)


def apt_cowthink():
    """Another cow-related easter egg"""
    print("  ___________________________")
    print("< I think, therefore I apt. >")
    print("  ---------------------------")
    print("         \\   ^__^")
    print("          \\  (oo)\\_______")
    print("             (__)\\       )\\/\\")
    print("                 ||----w |")
    print("                 ||     ||")


def apt_fortune():
    """Random apt-related fortune"""
    import random
    fortunes = [
        "A package in the hand is worth two in the repo.",
        "To apt or not to apt, that is the question.",
        "With great power comes great package management.",
        "Keep calm and apt-get install.",
        "There is no place like ~/",
        "In Windows we trust, in apt we believe.",
        "May the --force be with you.",
        "sudo make me a sandwich.",
        "rm -rf / is not a dance move.",
        "This is not the package you are looking for.",
        "I find your lack of updates disturbing.",
        "One does not simply apt-get install everything.",
        "Winter is coming... update your packages.",
        "A Lannister always pays his dependencies.",
        "I am the one who apt-gets.",
        "Say my name: apt-get.",
        "I am Groot. (Translation: apt install tree)",
        "Why so serious? Just apt-get moo.",
        "Houston, we have a dependency problem.",
        "To infinity and beyond... with winget!",
        "I'll be back... after this update.",
        "Hasta la vista, outdated packages.",
        "You can't handle the truth! (But you can handle apt update)",
        "Life is like a box of chocolates... you never know what dependencies you'll get.",
        "Here's looking at you, package.",
        "May the packages be ever in your favor.",
        "I am inevitable. (Said every security update ever)",
        "I love the smell of freshly installed packages in the morning.",
        "You've got to ask yourself one question: 'Do I feel lucky?' Well, do ya, apt?",
        "Show me the packages!",
        "You complete me. (Said dependency to package)",
        "There's no crying in package management!",
        "You had me at 'apt update'.",
        "Carpe Diem. Seize the packages.",
        "Elementary, my dear Watson. The solution is apt-get install.",
        "Frankly, my dear, I don't give a damn... about outdated software.",
        "I'm gonna make him an offer he can't refuse: a system update.",
        "Bond. James Bond. License to install.",
        "ET phone home... to check for updates.",
        "Hakuna Matata. It means no worries... about dependencies.",
        "Just keep swimming... just keep updating.",
        "To the window, to the wall... 'til the packages install, y'all.",
        "I came, I saw, I apt-get installed.",
        "All you need is love... and a good package manager.",
        "The cake is a lie, but apt is real.",
        "It's dangerous to go alone! Take apt.",
        "Do a barrel roll! (apt update)",
        "The mitochondria is the powerhouse of the cell. apt is the powerhouse of the OS.",
        "Roses are red, violets are blue, apt update, and upgrade too.",
        "An apt a day keeps the doctor away.",
        "Better late than never, but better now than later. apt update!",
    ]
    print(f'  "{random.choice(fortunes)}"')
    print()
    print("         \\   ^__^")
    print("          \\  (oo)\\_______")
    print("             (__)\\       )\\/\\")
    print("                 ||----w |")
    print("                 ||     ||")


def apt_holiday():
    """Holiday easter egg"""
    import datetime
    now = datetime.datetime.now()

    if now.month == 12 and now.day == 25:
        print("Merry Christmas! Have you updated your packages today?")
    elif now.month == 1 and now.day == 1:
        print("Happy New Year! Time for a fresh apt update!")
    elif now.month == 10 and now.day == 31:
        print("Happy Halloween! Beware of spooky outdated packages!")
    elif now.month == 4 and now.day == 1:
        print("April Fools! Your packages have been... just kidding, run apt update.")
    elif now.month == 2 and now.day == 14:
        print("Happy Valentine's Day! apt loves you.")
    else:
        print("Today is a good day to update your packages!")


def apt_xkcd():
    """XKCD reference"""
    print("  [sudo] password for user: ********")
    print("  [sudo] password for user: ********")
    print("  [sudo] password for user: ********")
    print("  sudo: 3 incorrect password attempts")
    print()
    print("  (This is a reference to XKCD #149: Sandwich)")
    print("  https://xkcd.com/149/")


def apt_sudo():
    """Sudo easter egg"""
    print("  We trust you have received the usual lecture from the local System")
    print("  Administrator. It usually boils down to these three things:")
    print()
    print("      #1) Respect the privacy of others.")
    print("      #2) Think before you type.")
    print("      #3) With great power comes great responsibility.")
    print()
    print("  (sudo is not needed on Windows, but the spirit remains!)")


def apt_coffee():
    """Coffee break easter egg"""
    print("  ( ( (")
    print("   ) ) )")
    print("  ( ( (")
    print("   ) ) )")
    print("  |====|")
    print("  |    |")
    print("  |apt |")
    print("  |====|")
    print("   |  |")
    print("   |  |")
    print("   |__|")
    print("  (____)")
    print()
    print("  Time for a coffee break while packages install...")


def apt_matrix():
    """Matrix reference"""
    print("  Wake up, Neo...")
    print("  The Matrix has you...")
    print("  Follow the white rabbit.")
    print()
    print("  Knock, knock, Neo.")
    print()
    print("  (apt update: There is no spoon.)")


def apt_starwars():
    """Star Wars crawl"""
    print("  A long time ago in a package manager far, far away...")
    print()
    print("  EPISODE IV: A NEW APT")
    print()
    print("  It is a period of civil war. Rebel packages, striking")
    print("  from a hidden base, have won their first victory against")
    print("  the evil Windows Empire.")
    print()
    print("  During the battle, Rebel spies managed to steal secret")
    print("  plans to the Empire's ultimate weapon, the APT DEATH STAR,")
    print("  an armored package manager with enough power to destroy")
    print("  an entire operating system.")
    print()
    print("  Pursued by the Empire's sinister agents, Princess Package")
    print("  races home aboard her starship, custodian of the stolen")
    print("  plans that can save her people and restore freedom to")
    print("  the galaxy....")


def apt_hello():
    """Hello world easter egg"""
    print("  Hello, World!")
    print("  Hello, Package!")
    print("  Hello, apt!")
    print()
    print("  The traditional first program in any package manager.")


def apt_rickroll():
    """Never gonna give you up"""
    print("  Never gonna give you up")
    print("  Never gonna let you down")
    print("  Never gonna run around and desert you")
    print("  Never gonna make you cry")
    print("  Never gonna say goodbye")
    print("  Never gonna tell a lie and hurt you")
    print()
    print("  (You've been apt-rolled!)")


def apt_docker():
    """Docker reference"""
    print('  "It works on my machine."')
    print('  "Then we\'ll ship your machine."')
    print()
    print("  (Docker solves this. apt solves the rest.)")


def apt_vim():
    """Vim easter egg"""
    print("  :q")
    print("  :q!")
    print("  :wq")
    print("  ZZ")
    print("  :x")
    print()
    print("  (How do I exit vim?)")
    print("  (Don't worry, apt doesn't use vim... or does it?)")


def apt_emacs():
    """Emacs easter egg"""
    print("  Emacs is a great operating system, lacking only a good text editor.")
    print()
    print("  (apt is a great package manager, lacking only... nothing. It's perfect.)")


def apt_arch():
    """Arch Linux reference"""
    print('  "I use Arch, btw."')
    print()
    print("  (We get it. You use Arch. But do you use apt?)")


def apt_gentoo():
    """Gentoo reference"""
    print('  "I use Gentoo. I compile everything from source."')
    print()
    print("  (That's nice. Meanwhile, apt install firefox took 30 seconds.)")


def apt_ubuntu():
    """Ubuntu reference"""
    print("  \"Ubuntu is an ancient African word meaning 'I can't configure Debian'.\"")
    print()
    print("  (But with apt, you don't need to configure anything!)")


def apt_debian():
    """Debian reference"""
    print('  "Debian: The Universal Operating System."')
    print('  "apt: The Universal Package Manager."')
    print()
    print("  (Now available on Windows!)")


def apt_windows():
    """Windows reference"""
    print('  "Windows is not a bug, it\'s a feature."')
    print()
    print("  (But with apt on Windows, it's definitely a feature!)")


def apt_linux():
    """Linux reference"""
    print('  "Linux is user-friendly. It\'s just very selective about who its friends are."')
    print()
    print("  (apt is friends with everyone. Even Windows users.)")


def apt_bash():
    """Bash reference"""
    print('  "With a shell, a user is never alone."')
    print()
    print("  (With apt, a user is never outdated.)")


def apt_python():
    """Python reference"""
    print("  import apt")
    print("  apt.update()")
    print("  apt.install('happiness')")
    print()
    print("  (This code is self-documenting.)")


def apt_c():
    """C reference"""
    print("  #include <apt.h>")
    print("  int main() {")
    print('      apt_update();')
    print('      apt_install("happiness");')
    print("      return 0;")
    print("  }")
    print()
    print("  (Segmentation fault (core dumped))")
    print("  (Just kidding, apt is written in Python. No segfaults here!)")


def apt_java():
    """Java reference"""
    print("  public class Apt {")
    print("      public static void main(String[] args) {")
    print("          AptManager apt = new AptManagerFactory()")
    print("              .getAptManagerBuilder()")
    print("              .build();")
    print("          apt.update();")
    print("      }")
    print("  }")
    print()
    print("  (FactoryFactoryFactory not included.)")


def apt_javascript():
    """JavaScript reference"""
    print("  npm install apt")
    print("  const apt = require('apt')")
    print("  apt.update().then(() => {")
    print("      console.log('Done!')")
    print("  }).catch(err => {")
    print("      console.error('Dependency hell!')")
    print("  })")
    print()
    print("  (left-pad not included.)")


def apt_rust():
    """Rust reference"""
    print("  fn main() {")
    print("      let apt = Apt::new();")
    print("      apt.update().unwrap();")
    print("  }")
    print()
    print("  (borrow checker approved.)")


def apt_go():
    """Go reference"""
    print("  package main")
    print('  import "apt"')
    print("  func main() {")
    print("      apt.Update()")
    print("  }")
    print()
    print("  (if err != nil { panic(err) })")


def apt_ruby():
    """Ruby reference"""
    print("  require 'apt'")
    print("  apt = Apt.new")
    print("  apt.update!")
    print()
    print("  (There's more than one way to do it.)")


def apt_php():
    """PHP reference"""
    print("  <?php")
    print("  $apt = new Apt();")
    print("  $apt->update();")
    print("  ?>")
    print()
    print("  (PHP is the best language for web development.")
    print("  (Fight me.)")


def apt_perl():
    """Perl reference"""
    print("  #!/usr/bin/perl")
    print("  use Apt;")
    print("  my $apt = Apt->new;")
    print("  $apt->update;")
    print()
    print("  (There's more than one way to do it, but this way is the most cryptic.)")


def apt_haskell():
    """Haskell reference"""
    print("  main = do")
    print("      let apt = Apt.new")
    print("      apt.update")
    print()
    print("  (This code is purely functional.)")


def apt_lisp():
    """Lisp reference"""
    print("  (apt-update)")
    print("  (apt-install 'happiness)")
    print()
    print("  (Lots of Irritating Single Parentheses)")


def apt_brainfuck():
    """Brainfuck reference"""
    print("  ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.")
    print("  >+.+++++++..+++.>++.<<+++++++++++++++.>.")
    print("  +++.------.--------.>+.>.")
    print()
    print("  (Translation: apt update)")
    print("  (Don't ask me how I know this.)")


def apt_morse():
    """Morse code easter egg"""
    print("  .- .--. - / ..- .--. -.. .- - .")
    print()
    print("  (apt update in Morse code)")


def apt_binary():
    """Binary easter egg"""
    print("  01100001 01110000 01110100 00100000")
    print("  01110101 01110000 01100100 01100001 01110100 01100101")
    print()
    print("  (apt update in binary)")


def apt_hex():
    """Hex easter egg"""
    print("  61 70 74 20 75 70 64 61 74 65")
    print()
    print("  (apt update in hex)")


def apt_base64():
    """Base64 easter egg"""
    print("  YXB0IHVwZGF0ZQ==")
    print()
    print("  (apt update in base64)")


def apt_rot13():
    """ROT13 easter egg"""
    print("  ncg hcqngr")
    print()
    print("  (apt update in ROT13)")


def apt_piglatin():
    """Pig Latin easter egg"""
    print("  aptway updateway")
    print()
    print("  (apt update in Pig Latin)")


def apt_yoda():
    """Yoda speak easter egg"""
    print("  Update your packages, you must.")
    print("  Outdated software, the path to the dark side is.")
    print("  Fear leads to anger. Anger leads to hate.")
    print("  Hate leads to broken dependencies.")
    print()
    print("  (May the --force be with you.)")


def apt_gandalf():
    """Gandalf easter egg"""
    print('  "You shall not pass!" (said the firewall)')
    print('  "But I have apt!" (said the user)')
    print()
    print("  (One does not simply walk into Mordor without updating first.)")


def apt_dumbledore():
    """Dumbledore easter egg"""
    print('  "Happiness can be found even in the darkest of times,')
    print("   if one only remembers to turn on the light...")
    print('   and run apt update."')


def apt_snape():
    """Snape easter egg"""
    print('  "Turn to page 394... of the apt manual."')


def apt_harrypotter():
    """Harry Potter easter egg"""
    print('  "You\'re a package manager, Harry."')
    print('  "I\'m a what?"')
    print('  "A package manager. And a thumping good one at that."')


def apt_lotr():
    """Lord of the Rings easter egg"""
    print('  "One Ring to rule them all, One Ring to find them,')
    print("   One Ring to bring them all and in the darkness bind them.")
    print('   One apt to update them all..."')


def apt_got():
    """Game of Thrones easter egg"""
    print('  "Winter is coming... and so are security updates."')
    print('  "A Lannister always pays his dependencies."')
    print('  "You know nothing, Jon Snow... about package management."')


def apt_breakingbad():
    """Breaking Bad easter egg"""
    print('  "I am the one who apt-gets."')
    print('  "Say my name."')
    print('  "apt-get."')
    print('  "You\'re goddamn right."')


def apt_simpsons():
    """Simpsons easter egg"""
    print('  "D\'oh! I forgot to run apt update!"')
    print('  "Why you little... outdated package!"')
    print('  "Mmm... fresh packages."')


def apt_futurama():
    """Futurama easter egg"""
    print('  "Good news, everyone! I\'ve invented a package manager')
    print("   that makes you read these messages while you wait!\"")


def apt_rickmorty():
    """Rick and Morty easter egg"""
    print('  "Wubba lubba dub dub!"')
    print('  "I\'m Pickle Rick! And I use apt!"')
    print('  "To live is to risk it all. Otherwise, you\'re just an inert chunk of')
    print("   randomly assembled molecules drifting wherever the universe")
    print('   blows you... without apt."')


def apt_southpark():
    """South Park easter egg"""
    print('  "Oh my God! They killed apt!"')
    print('  "You bastards!"')


def apt_spongebob():
    """SpongeBob easter egg"""
    print('  "I\'m ready! I\'m ready! I\'m ready!"')
    print('  "To update my packages!"')


def apt_pokemon():
    """Pokemon easter egg"""
    print('  "Gotta catch \'em all!"')
    print('  "Gotta update \'em all!"')
    print('  "Pikachu, use apt update!"')


def apt_mario():
    """Mario easter egg"""
    print('  "It\'s-a me, apt!"')
    print('  "Let\'s-a update!"')
    print('  "Thank you so much for to playing my package manager!"')


def apt_zelda():
    """Zelda easter egg"""
    print('  "It\'s dangerous to go alone! Take apt."')
    print('  "Hey! Listen! You need to update your packages!"')


def apt_minecraft():
    """Minecraft easter egg"""
    print('  "Creeper?"')
    print('  "Aww man..."')
    print('  "So we back in the mine, got our pickaxe swinging from side to side..."')
    print('  "Side, side to side..."')
    print('  "This task a grueling one, hope to find some diamonds tonight..."')
    print('  "Diamonds tonight..."')
    print('  "Heads up, you hear a sound, turn around and look up..."')
    print('  "Total shock fills your body..."')
    print('  "Oh no it\'s you again, I could never forget those eyes, eyes, eyes..."')
    print('  "Eyes, eyes, eyes..."')
    print('  "Cause baby tonight, the creeper\'s trying to steal all our stuff again..."')
    print('  "Cause baby tonight, you grab your pick, shovel and bolt again..."')
    print('  "And run, run until it\'s done, done, until the sun comes up in the morn..."')
    print('  "Cause baby tonight, the creeper\'s trying to steal all our stuff again..."')
    print()
    print("  (apt update: Now playing Revenge by CaptainSparklez)")


def apt_tetris():
    """Tetris easter egg"""
    print("  ████")
    print("  ████")
    print("  ████")
    print("  ████")
    print()
    print("  (Tetris block: I-piece)")
    print("  (apt update: Line clear!)")


def apt_pacman():
    """Pacman easter egg"""
    print("  <=======<  o  >=======>")
    print()
    print("  (Pac-Man is eating your outdated packages!)")


def apt_spaceinvaders():
    """Space Invaders easter egg"""
    print("    ▀▄   ▄▀")
    print("   ▄█▀███▀█▄")
    print("  █▀███████▀█")
    print("  █ █▀▀▀▀▀█ █")
    print("     ▀▀ ▀▀")
    print()
    print("  (Space Invaders are attacking your system!)")
    print("  (apt update: Pew pew pew!)")


def apt_doom():
    """DOOM easter egg"""
    print('  "Rip and tear, until it is done."')
    print('  "Rip and tear your outdated packages!"')
    print()
    print("  (DOOM music intensifies)")


def apt_portal():
    """Portal easter egg"""
    print('  "The cake is a lie."')
    print('  "But apt is real."')
    print()
    print('  "This was a triumph."')
    print("  \"I'm making a note here: HUGE SUCCESS.\"")
    print('  "It\'s hard to overstate my satisfaction."')
    print('  "Apt Science: We do what we must because we can."')


def apt_halflife():
    """Half-Life easter egg"""
    print('  "Rise and shine, Mr. Freeman. Rise and shine."')
    print('  "Not that I wish to imply you have been sleeping on the job."')
    print('   "No one is more deserving of a rest."')
    print('  "But apt update waits for no one."')


def apt_counterstrike():
    """Counter-Strike easter egg"""
    print('  "Counter-Terrorists win!"')
    print('  "Terrorists win!"')
    print('  "apt update wins!"')


def apt_fortnite():
    """Fortnite easter egg"""
    print('  "Victory Royale!"')
    print('  "You just won by updating all your packages!"')


def apt_amongus():
    """Among Us easter egg"""
    print("  .  .")
    print("  |__|")
    print(" /    \\")
    print("|  ()  |")
    print(" \\____/")
    print("  |  |")
    print("  |  |")
    print()
    print("  (Red is sus. He didn't run apt update.)")


def apt_shrek():
    """Shrek easter egg"""
    print('  "Ogres are like onions."')
    print('  "They have layers."')
    print('  "Like apt has layers of dependencies."')
    print()
    print('  "What are you doing in my swamp?!"')
    print('  "I\'m updating packages, Shrek!"')


def apt_bee():
    """Bee Movie easter egg"""
    print('  "According to all known laws of aviation,')
    print("   there is no way a bee should be able to fly.")
    print('  "Its wings are too small to get its fat little body off the ground."')
    print('  "The bee, of course, flies anyway because bees don\'t care')
    print("   what humans think is impossible.")
    print()
    print("  (apt update: Bee-lieve in yourself!)")


def apt_minions():
    """Minions easter egg"""
    print("  Banana! Banana! Banana!")
    print("  Poopaye! Poopaye!")
    print("  Tulaliloo ti amo!")
    print()
    print("  (Minions are updating your packages...)")


def apt_emoji():
    """Emoji easter egg"""
    print("  🐄🐄🐄🐄🐄")
    print("  🐄 apt moo 🐄")
    print("  🐄🐄🐄🐄🐄")
    print()
    print("  (Moo!)")


def apt_ascii_art():
    """Random ASCII art"""
    import random
    arts = [
        r"""
    /\_/\
   ( o.o )
    > ^ <
        """,
        r"""
     /\_____/\
    /  o   o  \
   ( ==  ^  == )
    )         (
   (           )
  ( (  )   (  ) )
 (__(__)___(__)__)
        """,
        r"""
    |\__/,|   (`\
  _.|o o  |_   ) )
-(((---(((--------
        """,
        r"""
       \    /\
        )  ( ')
       (  /  )
        \(__)|
        """,
        r"""
   _____
  |  o o|
  |  >  |
  | \_/ |
   || ||
  /| | |\
 (_/ |_|\_)
        """,
    ]
    print(random.choice(arts))
    print("  (Random ASCII art brought to you by apt)")


def apt_random_easter_egg():
    """Random easter egg"""
    import random
    eggs = [
        apt_fortune, apt_coffee, apt_matrix, apt_starwars,
        apt_hello, apt_rickroll, apt_docker, apt_vim, apt_emacs,
        apt_arch, apt_gentoo, apt_ubuntu, apt_debian, apt_windows,
        apt_linux, apt_bash, apt_python, apt_c, apt_java,
        apt_javascript, apt_rust, apt_go, apt_ruby, apt_php,
        apt_perl, apt_haskell, apt_lisp, apt_brainfuck, apt_morse,
        apt_binary, apt_hex, apt_base64, apt_rot13, apt_piglatin,
        apt_yoda, apt_gandalf, apt_dumbledore, apt_snape,
        apt_harrypotter, apt_lotr, apt_got, apt_breakingbad,
        apt_simpsons, apt_futurama, apt_rickmorty, apt_southpark,
        apt_spongebob, apt_pokemon, apt_mario, apt_zelda,
        apt_minecraft, apt_tetris, apt_pacman, apt_spaceinvaders,
        apt_doom, apt_portal, apt_halflife, apt_counterstrike,
        apt_fortnite, apt_amongus, apt_shrek, apt_bee,
        apt_minions, apt_emoji, apt_ascii_art,
    ]
    random.choice(eggs)()

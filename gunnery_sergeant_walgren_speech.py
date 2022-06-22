import sys
import time
import os

speech = """[inaudible] we got to be done with this.\n\
[inaudible] camera. Worst combat camera [inaudible].\n\
Marine, you're done. Cameras off.\n\
[inaudible] No, negative. Negative.\n\n\
I agree with one thing that's been said, and it is about how good you look.\n\
These cammies make my butt look @!*@ing awesome.\n\
I see a whole bunch of do-rags, that motivates the @!*@ out of me.\n\
@!*@in' professionals.\n\
Quiet professionals, is that what we're called?\n\
I think y'all are some crazy God-@*!@ mother-@!*@ers!\n\
Not one speech--now we've been talking about this, I'm kind of upset about the general's speech, I'm kind of upset about the Battalion commander's speech.\n\
I haven't gotten any @!*@ing goosebumps yet.\n\
Have y'all been motivated about this?\n\n\
I know y'all figured out another secret that the Marine Corps has.\n\
We don't tell you @!*@.\n\
And we play games.\n\
Man, I knew we were leaving tonight... @!*@ing seven months ago!\n\
[inaudible] didn't tell y'all because we want you to get @!*@ing pissed off.\n\
You might be envisioning US when you kill the enemy.\n\
But mother-@!*@er, you're going to be pissed.\n\n\
Marjah… @!*@ that.\n\
What do y'all want to hear--y'all want to hear the White Sleeves?\n\
I'm not doing the @!*@ing White Sleeves.\n\
We got to @!*@ing step across this parade deck and it's God-@!*@ cold.\n\
I'm not doing that @!*@.\n\
[inaudible] I don't like you.\n\n\
The White Sleeves--that's too long--y'all know John Glenn's speech, right, did I tell you that yet?\n\
Alright, we'll do that. We'll do that real quick.\n\n\
[Gunnery Sergeant Walgren throws his cigar onto the ground.]\n\n\
Who knows who John Glenn is?\n\
I ain't got time--John Glenn.\n\
John Glenn.\n\
First American to orbit the Earth in space.\n\
Was a senator for the state of Ohio.\n\
Oldest man to go back up into space, ‘cause he's a PT god.\n\
Before all of that, he was a @!*@in’ Marine.\n\n\
...an air-winger, though, a pilot.\n\n\
Right, [inaudible]?\n\
[inaudible] that camera, get the @!*@ away from me!\n\n\
John Glenn, 1974, ran for senate.\n\
Against a politician named Howard Metzenbaum.\n\
Howard Metzenbaum, was a sorry mother-@!*@er.\n\
John Glenn at this point, was a Marine. First American to orbit the Earth in space.\n\
Howard Metzenbaum asked him, ”How could you run for senate when you’ve never held a job.”\n\
What the @!*@ would you do if someone said that @!*@ to you?\n\
Now I’m going to change a little bit of this, I can, it’s my world.\n\n\
John Glenn said, ”Is that right?"\n\
”I served 23 years in the United States Marine Corps.”\n\
”I fought through 2 wars.”\n\
”I flew 149 missions.”\n\
”My plane was hit by an aircraft fire on 12 different occasions.”\n\
”I was in the space program.”\n\n\
”It wasn’t my JOB.”\n\
”It was my LIFE that was on the line!”\n\n\
”And this wasn’t a 9-to-5 job where I can take time off to take the daily cash receipts to the bank!”\n\n\
”I ask you to come with me as I was the other day to a veterans hospital.”\n\
”And you stand there. You look at those men with their mangled bodies.”\n\
”You look them in the eye and tell them that they never had a job.”\n\
”You come with me and visit any Gold Star mother.”\n\
”You look her in the eye and tell her, her son never held a job.”\n\
”You come with me to the space program and visit the widows and the orphans of Ed White, Gus Grissom and Roger Chaffee.”\n\
”And you look those kids in the eyes and tell them that their dads never held a job.”\n\
”You come with me on this memorial day weekend coming up, to Arlington National Cemetery, where I got more friends than I’d like to remember.”\n\
”And you stand there.”\n\
”You watch those waving flags.”\n\
”You think about this nation.”\n\
”And you tell me that THOSE people never held a job.”\n\n\
@!*@!\n\n\
"I’ll tell you, Howard Metzenbaum."\n\
"You should be on your knees, every day of your life, thanking GOD, that there are some men who have held a job."\n\
"And they require the DEDICATION OF PURPOSE, a LOVE OF COUNTRY and DEDICATION OF DUTY, that was MORE IMPORTANT THAN LIFE ITSELF."\n\n\
"THEIR SELF SACRIFICE IS WHAT MADE THIS COUNTRY @!*@ING POSSIBLE."\n\n\
Isn’t that badass!?\n\
@!*@ you all!--ISN’T THAT BADASS!?\n\n\
Okay, roger that, [inaudible] are you motivated?\n\
I see your do-rag [inaudible].\n\
Alright, ”quiet professionals”--@!*@ all that.\n\
@!*@ all this talk about doing what you’ve been trained to do.\n\
You all know @!*@ well you get out there and you @!*@ing do @!*@ because of the Marine to your left, and the Marine to your @!*@ing right. God, Country and Corps don’t matter at that @!*@ing point.\n\
Let the Taliban throw the women and children in front. We won’t shoot.\n\
We’ll just @!*@ing creep out around them but with a cup of coffee, slap them on the @!*@ing shoulder and say, ”What the @!*@ is your problem, @!*@!*!?”\n\
@!*@ them! Let them try to fight the United States Marine Corps conventional.\n\
What the @!*@ is wrong with their… the… stupid mother-@!*@ers!\n\
Shoot at me! Bring the AA gun down, @!*@!*, let’s @!*@in’ do this!\n\
You’re going to do what you need to do for @!*@in’ each other.\n\
Not for anybody else.\n\
And if tomorrow, or maybe in a couple of days it might take a little bit longer than that, the people of Marjah will be on their knees every day of their @!*@in’ life, thanking God, that angry…\n\n\
The string has been cut loose.\n\
They can’t @!*@in’ stop us now!\n\
What the @!*@ are they gonna to do now!?\n\n\
@!*@, @!*@ you, get up.\n"""

def written_speech(speech):
    for char in speech:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

written_speech(speech)

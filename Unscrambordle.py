#Unscramordle by maybeinactive
print("Welcome to Unscramordle!\n")
import random as r
WordList = [
	"above",
	"abuse",
	"adopt",
	"adult",
	"agent",
	"anger",
	"ample",
	"beach",
	"bingo",
	"biome",
	"birth",
	"block",
	"board",
	"brain",
	"bread",
	"break",
	"brown",
	"buyer",
	"cause",
	"chain",
	"chair",
	"chase",
	"chest",
	"chief",
	"child",
	"china",
	"claim",
	"coast",
	"court",
	"cover",
	"crane",
	"cream",
	"crime",
	"crowd",
	"crown",
	"dance",
	"death",
	"depth",
	"doubt",
	"draft",
	"dream",
	"drink",
	"drive",
	"earth",
	"enter",
	"faith",
	"fault",
	"field",
	"fight",
	"final",
	"focus",
	"force",
	"flame",
	"frame",
	"front",
	"fruit",
	"group",
	"guide",
	"heart",
	"horse",
	"hotel",
	"house",
	"image",
	"input",
	"judge",
	"knife",
	"layer",
	"light",
	"lunch",
	"major",
	"march",
	"match",
	"metal",
	"mines",
	"model",
	"money",
	"month",
	"mouth",
	"music",
	"night",
	"noise",
	"north",
	"novel",
	"nurse",
	"olive",
	"order",
	"other",
	"owner",
	"panel",
	"party",
	"phase",
	"phone",
	"pilot",
	"pitch",
	"place",
	"plane",
	"plant",
	"plate",
	"point",
	"pound",
	"power",
	"price",
	"pride",
	"radio",
	"range",
	"ratio",
	"ready",
	"reply",
	"right",
	"river",
	"round",
	"route",
	"scale",
	"score",
	"shape",
	"share",
	"shift",
	"shirt",
	"shock",
	"sight",
	"smile",
	"smoke",
	"sound",
	"south",
	"space",
	"sport",
	"squad",
	"stage",
	"steam",
	"stock",
	"stone",
	"store",
	"study",
	"style",
	"sugar",
	"table",
	"thing",
	"touch",
	"tower",
	"track",
	"trade",
	"train",
	"trend",
	"trial",
	"uncle",
	"unity",
	"value",
	"video",
	"voice",
	"waste",
	"watch",
	"water",
	"while",
	"white",
	"whole",
	"woman",
]
SolvedGuess = []
SolveHint = 0
ChosenWord = "".join(map(str, r.choices(WordList)))

def MainGame(Word, Guesses, SolutionHint): #Var + Hints
	if len(Guesses) >= 3:
		SolutionHint = 2
	else:
		SolutionHint = 0
	WordLister = list(Word)
	WordHint = WordLister
	WordHint.insert(0, "_")
	print("\033[1;37m"+WordLister[1]+" "+WordHint[SolutionHint]+" _ _ _")
	PlayerGuess = str(input())
	GuessLister = list(PlayerGuess)
	FinalLister=list(set(GuessLister)&set(WordLister))
	if len(PlayerGuess) == 5: #GuessChecker
		if PlayerGuess == Word: 
			print("\033[1;32m"+"Win! The word was "+Word+"\n")
			Word = "".join(map(str, r.choices(WordList)))
			Guesses.clear()
			MainGame(Word,Guesses, SolutionHint)
		else:
				for i in FinalLister:
					if i not in Guesses:
						Guesses.append(i)
		r.shuffle(Guesses)
		print("\033[1;35m"+str(Guesses)+"\033[0;37m"+"\n")
		MainGame(Word, Guesses, SolutionHint)
	else: #FailSafe
		print("Please enter a valid 5 letter word! \n")
		MainGame(Word, Guesses, SolutionHint)
MainGame(ChosenWord, SolvedGuess, SolveHint)
import random

def getKey(passedList):
	key = random.sample(range(100),len(passedList))
	return key
	pass


def getInput(): #This gets the inputs from the user
	userInput = input(" What would you like to encrypt?: ")
	listInput = list(userInput)
	for q in listInput:
		print(q)
	return listInput
	pass

def encryptInput(listToEncrypt, keyToUse):
	encryptedList = []
	for i,j in zip(listToEncrypt, keyToUse):
		output = i*j
		encryptedList.append(output)
	print("This is your encrypted phrase")
	print(encryptedList)
	return encryptedList

	pass

def assignInput(listToAssign, alphabet):
	#print(listToAssign)
	#print(alphabet)
	assignedList = []
	for i in listToAssign:
		for j in alphabet:
			if i == j:
				assignedList.append(alphabet.get(j))
	return assignedList
def decryption(returnedKey, returnedEncryption):

	decryptedInput = []
	for k,l in zip(returnedKey, returnedEncryption):
		newOutput = l/k
		decryptedInput.append(int(newOutput))
	return decryptedInput

	pass
def decryptionOption():
	UserAnswer = input("Would you like to decrypt? (y/n): ").upper()
	return UserAnswer
def getDecryptedOutput(alphabet, decryptedInputToAssign):
	decryptedOutput = []
	for l in decryptedInputToAssign:
		for m in alphabet:
			if l == alphabet.get(m):
				decryptedOutput.append(m)
	print("this is the decryptedOutput")
	print(decryptedOutput)
	return decryptedOutput
	pass
def main():
	alphabet = {
	'A': 1,
	'B': 2,
	'C': 3,
	'D': 4,
	'E': 5,
	'F': 6,
	'G': 7,
	'H': 8,
	'I': 9, 
	'J': 10,
	'K': 11,
	'L': 12,
	'M': 13,
	'N': 14,
	'O': 15, 
	'P': 16,
	'Q': 17,
	'R': 18,
	'S': 19,
	'T': 20,
	'U': 21,
	'V': 22,
	'W': 23,
	'X': 24,
	'Y': 25,
	'Z': 26,
	' ': 27,
	'a': 28,
	'b': 29,
	'c': 30,
	'd': 40,
	'e': 41,
	'f': 42,
	'g': 43,
	'h': 44,
	'i': 45,
	'j': 46,
	'k': 47,
	'l': 48,
	'm': 49,
	'n': 50,
	'o': 51,
	'p': 52,
	'q': 53,
	'r': 54,
	's': 55,
	't': 56,
	'u': 57,
	'v': 58,
	'w': 59,
	'x': 60,
	'y': 61,
	'z': 62,
	}
	returnedList = getInput()
	returnedKey = getKey(returnedList)
	numberedInput = assignInput(returnedList, alphabet)
	returnedEncryption = encryptInput(numberedInput, returnedKey)
	if decryptionOption() == "Y":
		decryptedInputToAssign = decryption(returnedKey, returnedEncryption)
	finalOutput = getDecryptedOutput(alphabet, decryptedInputToAssign)
	pass

if __name__ == '__main__':
	main()
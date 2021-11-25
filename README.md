# Mach8_Test

This is my solution to the Mach8 technical test.

## Test project

The project consist to write a function that searches through NBA player heights in inches based on user input. The data is served in json format by the endpoint [here](https://mach-eight.uc.r.appspot.com/).

The task is to create an application that takes a single integer input. The application will download the raw data from the [endpoint]
(https://mach-eight.uc.r.appspot.com) and print a list of all pairs of NBA players whose height in inches adds up to the integer input to the application. If no matches are found, the application will print "No matches found"

Sample output is as follows:
```
> app 139

- Brevin Knight         Nate Robinson
- Nate Robinson         Mike Wilks
```

The algorithm to find the pairs must be faster than O(n^2). All edge cases should be handled appropriately. Though not strictly required, demonstrating comfort in writing unit tests will make your submission stand out. This is **NOT** a closed book test. You are encouraged to reach out with any questions that you come across.

## The solution
My approach consist in sort ascending all players by his height in inches. Based in the characteristics of the player data, I considered a good idea keep track of groups of players with the same height in inches.

So, when a user input a height to search, the application will take the first player(player with lower height) and calculate the missing height as the input height minus the first player height. latter with that quantity will filter all player with the same height and are different from the first player, creating pairs with the first player and the other players.

To avoid the issue of getting pair of for example (Player 1, Player 2) and (Player 2, Player 1) as part of the solution the application will calculate position when started the filtered player set for the first played, in the whole sorted data, and will iterate from the first player until the calculated position minus 1.

The solution code, were designed using Pre-conceptual schema as domain modeler tool, Robustness diagram and classes diagram  to model the solution. These diagrams could be found in the folder "Design". The design, help a lot to take in account multiple edge cases, ease planing and implementation phases.

This was a very fun project and I enjoy it a lot.

## Installation
This installation guide is created to be executed in a Windows 10+ machine with Git and miniconda installed.

1. Download the GitHub repo:
	```
	git clone https://github.com/Lirb/Mach8_Test.git
	```
2. Go to the project folder:
	```
	cd path_to_cloned_folder/Mach8_test
	```
3. Create an python environment and install all dependencies:
	```
	conda create --name mach8_env --file requirements.txt
	```
4. Execute the project:
  the application expect the height as a execution argument.
  ```
	python -m app <height integer input>
	```
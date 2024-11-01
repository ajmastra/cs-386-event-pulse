#include <iostream>
using namespace std;

// create new struct patient
struct Patient
{
	// name
	string name;
	// age
	int age;
};

// class
class MedicalRecord
{
	// private 
	private:
		// pointer of array of patient type
		Patient* arrayData;
		// size of array
		int arraySize;
	// public
	public:
		// default constructor
		MedicalRecord() : arraySize(0)
		{
			// sets array to null
			arrayData = NULL;
		}
		// constructor with one argument
		MedicalRecord(int inArraySize) : arraySize(inArraySize)
		{
			// use new to make new array of size inArraySize
			arrayData = new Patient[inArraySize];
		}
		// copy constructor
		MedicalRecord(MedicalRecord& oldRecord)
		{
			// set array size to private size
			arraySize = oldRecord.arraySize;
			// set array to new array of size inArraySize
			arrayData = new Patient[arraySize];
			// iterate over all data
			for ( int i = 0; i < arraySize; i++ )
			{
				// copy over data
				arrayData[i] = oldRecord.arrayData[i];
			}
		}
		
		// deconstructor
		~MedicalRecord()
		{
			// delete array
			delete [] arrayData;
		}
		
		// accessor 
		int getArraySize()
		{
			return arraySize;
		}
		
		// get patient at index function
		Patient getPatientAt(int index)
		{
			return arrayData[index];
		}
		
		// operator overload
		Patient& operator[](int index)
		{
			// if the index is less than 0 
			if (index < 0)
			{
				// print error message
				cout << "Index out of range" << endl;
			}
			// otherwise, return data
			return arrayData[index];
		}
};



// main 
int main()
{
	// init variables
		// string for user input
	string userInput;
		// char for user char
	char userChar;
		// int for user int
	int userInt;
		// int for max users
	int maxUsers;
	// while the user char is not n
	while ( userChar != 'n' )
	{
		// print query to user
		cout << "How many users do you want to enter?\n>";
		cin >> maxUsers;
		cin.ignore();
		
		// init new medical records
		MedicalRecord record(maxUsers);
		// iterate through entire user quantity
		for ( int i = 0; i < maxUsers; i++ )
		{
			// query user for name
			cout << "Please type Patient " << i + 1 << "'s name\n> ";
			// get user name
			getline(cin, userInput);
			
			// query user for age
			cout << "Please type Patient " << i + 1 << "'s age\n> ";
			// get user age
			cin >> userInt;
			cin.ignore();
			
			// use overload to add new things into struct
			record[i] = {userInput, userInt};
		}
		
		// query user for an index number
		cout << "Please enter an index number (1-" << maxUsers;
		cout << ") to get patient information\n>";
		
		// get user input
		cin >> userInt;
		cin.ignore();
		// subtract 1 for the index
		userInt--;
		
		// find user age and then display the age at the index
		cout << "Name: " << record[userInt].name << " Age: ";
		cout << record[userInt].age << endl;
		
		// print title 
		cout << endl << "Now using copy constructor...\n";
		// use copy constructor
		MedicalRecord newRecord(record);
		
		// display the copy constructor
		cout << "Displaying copy constructor results\n";
		
		// iterate through all users to display copy
		for ( int i = 0; i < maxUsers; i++ )
		{
			// show name and age of current index
			cout << i + 1 << " User's Name: " << record[i].name << "\n";
			cout << i + 1 << " User's Age: " << record[i].age << endl;
		}
		
		// ask user if they want to input new records
		cout << endl << "Do you want to enter the records again? (y/n) \n";
		
		// get user input
		cin >> userChar;
		cin.ignore();
		
	}	
	return 0;
}

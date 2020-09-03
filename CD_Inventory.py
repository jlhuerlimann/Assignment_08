#------------------------------------------#
# Title: Assignment08.py
# Desc: Assignment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Jurg Huerlimann 2020-Aug-31 added get_CD_info and FileIO functions
# Jurg Huerlimann 2020-Sep-02 added menu functions and writing to file
# Jurg Huerlimann 2020-Sep-02 added docstrings and pickle function
#------------------------------------------#

import pickle    #importing pickle to create a binary data file

# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []

#@staticmethod
class CD:
    def add_cdinfo():
        """Stores data about a CD:

            properties:
                cdID: (int) with CD ID
                cdTitle: (string) with the title of the CD
                cdArtist: (string) with the artist of the CD
                methods:

        """

        cdID = int(input('Enter ID: ').strip())
        cdTitle = input('What is the title of the CD: ').strip()
        cdArtist = input('What is the name of the Artist: ').strip()

        return cdID, cdTitle, cdArtist

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODO Add code to process data from a file    
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        try:
            with open(file_name, 'rb') as fileObj:
                data = pickle.load(fileObj)
                table.extend(data)
        except EOFError:
            print("File does not exist")
        except FileNotFoundError as e:
            print("\n CDInventory file does not exists.  Please save inventory do disk to create a file.\n")  
            print(type(e), e, e.__doc__, sep='\n')   

# TODO Add code to process data to a file
    @staticmethod
    def write_file(file_name, table):
        
        """ Function to write data from memory the cdinventory.txt file

          Args:
            file_name (string): string indicating the file name to write to
            table (list of dicts): list to remove entry from dictionary

          Returns:
            none
        """
 
        objFile = open(file_name, 'w')
        with open(file_name, 'wb') as objFile:  
            pickle.dump(table, objFile) 
          
        objFile.close()        
    
    @staticmethod
    def add_to_inventory(intID, strTitle, strArtist, table):
        """ Function to add data to in memory cd inventory

         Args:
            intID (string): string indicating ID of the new CD
            strTitle (string): string indicating Title of the new CD
            strArtist (string): string indicating Artist of the new CD
            table (list of dicts): list to append new dictionary entry to

         Returns:
            table (list of dicts): list of dictionaries with the new entry appended.
        """
        table.append({"ID": intID, "Title": strTitle, "Artist": strArtist})    

# -- PRESENTATION (Input/Output) -- #
class IO:

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        Args:
            None.
        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit\n')
        
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')    
# -- Main Body of Script -- #
        
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()

    if strChoice == 'x':
        break
    
    if strChoice == 'l':
        load = FileIO.read_file()
        if load:
            FileIO.read_file(strFileName, lstOfCDObjects)    
        else:
            input('\ncanceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        continue  # start loop back at top.  
    
    elif strChoice == 'a':
        cd_id, cd_title, cd_artist = CD.add_cdinfo()
        FileIO.add_to_inventory(cd_id, cd_title, cd_artist, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
        
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        FileIO.write_file(strFileName, lstOfCDObjects)
        continue  # start loop back at top.
    
    else:
         print('General Error')


# siemens_Q-2

Componentes Details :-

The circuit has 4 Resistors each having values of 1K ohm and 1% tolerance

DC power supply of 1.5V to inverting terminal and 2.5V to non inverting terminal

////////////////////////////////////////////////////////////////////////////////////////////////

Analysis and sequence of steps :-

-> Once the circuit is built we can simulate it by giving 1.5v and 2.5v for inverting and non inverting terminals respectively

-> Then we use .measure command and simulate it with python

-> By taking into account of tolerance levels of resistors we calculate max,min voltages

-> From the response graphs we can analyse the circuit and calculate the necessary values like gain etc.

///////////////////////////////////////////

Minimum, nominal, and maximum output voltage of the circuit are :-

Vo(min) = (2.5-1.5)*(1 - 40.01)-0.01 = -0.029V

Vo(nom) = 2.5-1.5 = 1V

Vo(max) = (2.5-1.5)*(1+40.01)+0.01 = 2.029V

//////////////////////////////////////////////////////////////////////////

Schematic diagram :-

![image](https://user-images.githubusercontent.com/117454960/235338122-255c43b2-0fbc-4d3a-91a8-7ea3b5d5f129.png)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Input :-

![image](https://user-images.githubusercontent.com/117454960/235338276-2dd827c4-8794-4e35-a553-e93339ee2d61.png)

Output :-

![image](https://user-images.githubusercontent.com/117454960/235338311-adf1b1d7-1312-481b-88ea-04cd8fbaa709.png)


using System;
using System.IO;

class Program {
  static int Part1(int[] datavalues, string[] datainst) {
    int[] currpos = {0,0};   //{Depth, Distance}
    for (int i=0;i<datavalues.Length;i++){
      if (datainst[i]=="forward") { //Increase Distance by X
        currpos[1] += datavalues[i];
      } else if (datainst[i]=="up") { //Decrease Depth by X
        currpos[0] -= datavalues[i];
      } else {  //Instruction must be "down". Increase Depth by X
        currpos[0] += datavalues[i];
      }
    }
    return currpos[0]*currpos[1]; //Final Answer = Depth * Distance
  }
  
  static int Part2(int[] datavalues, string[] datainst){
    int[] currpos = {0,0,0}; //{Aim, Depth, Distance}
    for (int i=0;i<datavalues.Length;i++) {
      if (datainst[i]=="forward") { //Forward increases Dist by X and Depth by X*aim
        currpos[2] += datavalues[i];
        currpos[1] += datavalues[i]*currpos[0];
      } else if (datainst[i]=="up") { //Decrease Aim by X
        currpos[0] -= datavalues[i];
      } else { //Instruction must be "down". Increase Aim by X
        currpos[0] += datavalues[i];
      }
    }
    return currpos[1]*currpos[2]; //Final answer = Depth * Distance
  }


  public static void Main (string[] args) {
    string[] datain = File.ReadAllLines("input.txt"); //Open the data as an array of strings.
    int[] datavalues = new int[datain.Length];//Prepare instruction-number array.
    string[] datainst = new string[datain.Length];//Prepare instruction array.
    for (int i=0;i<datain.Length;i++){
      string[] tempy = datain[i].Split(" ");//Split instruction from number.
      datavalues[i] = int.Parse(tempy[1]); //Store the integer of the number part.
      datainst[i] = tempy[0]; //Store the instruction part.

    }
    Console.WriteLine("Final answer for Part 1: "+Part1(datavalues, datainst));
    Console.WriteLine("Final answer for Part 2: "+Part2(datavalues, datainst));


  }
}

using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

class Program {
  static int part1 (int[] depths) {
    int Counter = 0;
    for (int i=0;i<depths.Length-1;i++){
      if (depths[i+1]>depths[i]) {
        Counter += 1;
      }
    }
    return Counter;
  }
  static int part2 (int[] depths) {
    int Counter = 0;
    for (int i=0;i<depths.Length-3;i++){
      if (depths[i+3]>depths[i]) {
        Counter += 1;
      }
    }
    return Counter;
  }
  public static void Main (string[] args) {
    string[] datain = File.ReadAllLines("input");
    int[] datasafe = new int[datain.Length];
    for (int i=0;i<datain.Length;i++){
      datasafe[i] = int.Parse(datain[i]);
    }
    Console.WriteLine("I found "+part1(datasafe)+" increases for Part 1.");
    Console.WriteLine("I found "+part2(datasafe)+" increases for Part 2.");
  }
}

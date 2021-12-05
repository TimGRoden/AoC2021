using System;
using System.IO;
using System.Collections.Generic;

class Program {
  static string[] keys(string[] inputs) {
    string gamma = "";
    string epsilon ="";
    for (int i=0;i<inputs[0].Length;i++) {
      int found0 = 0;
      int found1 = 0;
      for (int j=0;j<inputs.Length;j++) {
        if (inputs[j][i]=='0') {
          found0 += 1;
        } else {
          found1 += 1;
        }
      }
      if (found0>found1) {
        gamma += "0";
        epsilon += "1";
      } else {
        gamma += "1";
        epsilon += "0";
      }
    }
    string [] gesol = {gamma, epsilon};
    return gesol;
  }

  static string[] Filter (string[] inputs, int pos, char key) {
    List<string> outstore = new List<string>();
    for (int i=0;i<inputs.Length;i++) {
      if (inputs[i][pos]==key) {
        outstore.Add(inputs[i]);
      }
    }
    string[] output = new string[outstore.Count];
    for (int i=0;i<outstore.Count;i++) {
      output[i] = outstore[i];
    }
    return output;
  }

static List<string> FilterL (List<string> inputs, int pos, char key) {
    List<string> outstore = new List<string>();
    for (int i=0;i<inputs.Count;i++) {
      if (inputs[i][pos]==key) {
        outstore.Add(inputs[i]);
      }
    }
    return outstore;
  }

  static List<string> Listcopy (List<string> inputs) {
    List<string> output = new List<string>();
    for (int i=0;i<inputs.Count;i++) {
      output.Add(inputs[i]);
    }
  return output;
  }

  static string OGR (List<string> inputs) {
    List<string> possibles = new List<string>();
    for (int i=0;i<inputs.Count;i++) {
      possibles.Add(inputs[i]);
    }
    for (int i=0;i<inputs[0].Length;i++) {
      List<string> tempy = new List<string>();
      char gamma = '0';
      int found0 = 0;
      int found1 = 0;
      for (int k=0;k<possibles.Count;k++) {
        if (possibles[k][i]=='0') {
          found0 += 1;
        } else {
          found1 += 1;
        }
      }
      if (found0>found1) {
        gamma = '0';
      } else {
        gamma = '1';
      }
      tempy = FilterL(possibles,i,gamma);
      possibles = Listcopy(tempy);
    }
  return possibles[0];
  }

static string CSR (List<string> inputs) {
    List<string> possibles = new List<string>();
    for (int i=0;i<inputs.Count;i++) {
      possibles.Add(inputs[i]);
    }
    for (int i=0;i<inputs[0].Length;i++) {
      List<string> tempy = new List<string>();
      char gamma = '0';
      int found0 = 0;
      int found1 = 0;
      for (int k=0;k<possibles.Count;k++) {
        if (possibles[k][i]=='0') {
          found0 += 1;
        } else {
          found1 += 1;
        }
      }
      if (found0<found1) {
        gamma = '1';
      } else {
        gamma = '0';
      }
      tempy = FilterL(possibles,i,gamma);
      possibles = Listcopy(tempy);
    }
  return possibles[0];
  }

  public static void Main (string[] args) {
    string[] datain = File.ReadAllLines("input.txt"); //Open the data as an array of strings.
    string[] datasafe = new string[datain.Length];
    for (int i=0;i<datain.Length;i++) {
      datasafe[i]=datain[i];
    }
    string[] gesol = keys(datasafe);
    Console.WriteLine("::Part 1 Solution::");
    Console.WriteLine("Gamma: "+gesol[0]);
    Console.WriteLine("Epsilon: "+gesol[1]);
    
    
    List<string> datastr = new List<string>();
    for (int i=0;i<datasafe.Length;i++) {
      datastr.Add(datasafe[i]);
    }
    Console.WriteLine("::Part 2 Solution::");
    Console.WriteLine("OGR: "+OGR(datastr));
    Console.WriteLine("CSR: "+CSR(datastr));
  }
}

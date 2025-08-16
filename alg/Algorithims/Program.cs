// See https://aka.ms/new-console-template for more information
using System.Globalization;
using System.Numerics;

// This is a Fibonacci sequence algorithm that returns the index of the Fibonacci number
// that matches the input number. If the number is not a Fibonacci number, it returns -1.
int fibonacciSequence(BigInteger num)
{
    if (num < 0) return -1;

    BigInteger a = 0;
    BigInteger b = 1;
    int index = 1;

    while (a < num)
    {
        BigInteger temp = a;
        a = b;
        b = temp + b;
        index++;
    }

     return a == num ? index : -1;
}

Console.WriteLine(fibonacciSequence(4));
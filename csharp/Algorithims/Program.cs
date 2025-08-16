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

    return a == num ? index - 1 : -1;
}

Console.WriteLine("Fibonacci Sequence Index:");
Console.WriteLine(fibonacciSequence(21));

static void PascalPyramid()
{
    int rows = 10;

    int[][] pascal = new int[rows][];

    for (int i = 0; i < rows; i++)
    {
        pascal[i] = new int[i + 1];
        pascal[i][0] = 1;
        pascal[i][i] = 1;

        for (int j = 1; j < i; j++)
        {
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j];
        }
    }

    for (int i = 0; i < rows; i++)
    {

        for (int j = 0; j <= i; j++)
        {
            Console.Write(pascal[i][j] + " ");
        }
        Console.WriteLine();
    }
}
Console.WriteLine("Pascal's Pyramid:");
PascalPyramid();
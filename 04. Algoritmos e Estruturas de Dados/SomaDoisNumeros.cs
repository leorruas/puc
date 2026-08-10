using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite o primeiro número: ");
        string entrada1 = Console.ReadLine();
        
        Console.Write("Digite o segundo número: ");
        string entrada2 = Console.ReadLine();

        if (double.TryParse(entrada1, out double num1) && double.TryParse(entrada2, out double num2))
        {
            double soma = num1 + num2;
            Console.WriteLine($"A soma dos números é: {soma}");
        }
        else
        {
            Console.WriteLine("Erro: Um ou ambos os valores digitados não são números válidos.");
        }
    }
}

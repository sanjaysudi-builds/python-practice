{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMyfnSjgmaD9Mil8yt4HRWs",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SanjuDev07/python-practice/blob/main/python_codes.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_LWTkXQJ_xYz",
        "outputId": "bae3de84-932f-4889-8993-f686c6491214"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quadratic Equation: ax^2+bx+c=0\n",
            "Enter coefficient a:1\n",
            "Enter coefficient b:-3\n",
            "Enter coefficient c:2\n",
            "Discriminant= 1.0\n",
            "Roots are real and distinct\n",
            "Root 1 = 2.0\n",
            "Root 2 = 1.0\n"
          ]
        }
      ],
      "source": [
        "import math\n",
        "print(\"Quadratic Equation: ax^2+bx+c=0\")\n",
        "a = float(input(\"Enter coefficient a:\"))\n",
        "b = float(input(\"Enter coefficient b:\"))\n",
        "c = float(input(\"Enter coefficient c:\"))\n",
        "if a==0:\n",
        "  print(\"It is not a quadratic equation\")\n",
        "else:\n",
        "  d=b*b-4*a*c\n",
        "\n",
        "  print(\"Discriminant=\",d)\n",
        "\n",
        "  if d>0:\n",
        "    root1=(-b+math.sqrt(d))/(2*a)\n",
        "    root2=(-b-math.sqrt(d))/(2*a)\n",
        "    print(\"Roots are real and distinct\")\n",
        "    print(\"Root 1 =\",root1)\n",
        "    print(\"Root 2 =\",root2)\n",
        "  elif d==0:\n",
        "    root = -b/(2*a)\n",
        "    print(\"Roots are real and equal\")\n",
        "    print(\"Root=\",root)\n",
        "  else:\n",
        "    real =-b/(2*a)\n",
        "    imag=math.sqrt(-d)/(2*a)\n",
        "    print(\"Roots are complex\")\n",
        "    print(\"Root 1=\",real,\"+\",imag,\"i\")\n",
        "    print(\"Root 2=\",real,\"-\",imag,\"i\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print( \"Sum of first n Natural Numbers\")\n",
        "\n",
        "n=int(input(\"Enter value of n:\"))\n",
        "\n",
        "sum=0\n",
        "\n",
        "for i in range(1,n+1):\n",
        "  sum=sum+i\n",
        "\n",
        "print(\"Sum=\",sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H9iHH4FzD8Vt",
        "outputId": "3c6e0218-e6ff-4203-de74-04d6c308268c"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sum of first n Natural Numbers\n",
            "Enter value of n:5\n",
            "Sum= 15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Multiplicatoin Table\")\n",
        "\n",
        "n=int(input(\"Enter a number:\"))\n",
        "\n",
        "for i in range(1,11):\n",
        "  print(n,\"x\",\"=\",n*i)\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yKVYSUi1Fp8f",
        "outputId": "cbedbfef-373b-4ec2-fa2d-98f0c65c1fea"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Multiplicatoin Table\n",
            "Enter a number:5\n",
            "5 x = 5\n",
            "5 x = 10\n",
            "5 x = 15\n",
            "5 x = 20\n",
            "5 x = 25\n",
            "5 x = 30\n",
            "5 x = 35\n",
            "5 x = 40\n",
            "5 x = 45\n",
            "5 x = 50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Prime Number Check\")\n",
        "\n",
        "n=int(input(\"enter a number:\"))\n",
        "\n",
        "if n>1:\n",
        "  for i in range(2,n):\n",
        "    if n%i==0:\n",
        "       print(\"Not Prime\")\n",
        "       break\n",
        "  else:\n",
        "    print(\"Prime number\")\n",
        "else:\n",
        "   print(\"Not Prime\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x3tVSDuqGlMo",
        "outputId": "db446224-de1c-40a5-faa7-8c181d698db8"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Prime Number Check\n",
            "enter a number:7\n",
            "Prime number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def factorial(n):\n",
        "  if n==0 or n==1:\n",
        "    return 1\n",
        "  else:\n",
        "    return n*factorial(n-1)\n",
        "n=int(input(\"Enter a number:\"))\n",
        "print(\"Factorial=\",factorial(n))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sq1CTtIDJuPs",
        "outputId": "6b6209fc-f740-419d-be88-c67c392de2f1"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number:4\n",
            "Factorial= 24\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Square of a Number Using Exception Handling\")\n",
        "while True:\n",
        "  try:\n",
        "    n=int(input(\"Enter a number:\"))\n",
        "    square = n*n\n",
        "    print(\"Square=\",square)\n",
        "    break\n",
        "  except ValueError:\n",
        "    print(\"Invalid input.Please enter a valid integer.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bMwRLFvkK2XP",
        "outputId": "8dfe2341-c6a8-45f8-f509-c33189f3164d"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Square of a Number Using Exception Handling\n",
            "Enter a number:abbgv\n",
            "Invalid input.Please enter a valid integer.\n",
            "Enter a number:8\n",
            "Square= 64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Count Number of Vowels\")\n",
        "sentence=input(\"Enter a sentence:\")\n",
        "count=0\n",
        "for ch in sentence:\n",
        "  if ch in 'aeiouAEIOU':\n",
        "    count +=1\n",
        "print(\"Number of vowels=\",count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hcQGBvTvL27G",
        "outputId": "f043e5b9-e4d4-43da-e40a-0703c2df8350"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Count Number of Vowels\n",
            "Enter a sentence:sdfwetytgfrewefdsiu\n",
            "Number of vowels= 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Book List Operations\")\n",
        "books =[]\n",
        "for i in range(3):\n",
        "  title=input(\"Enter book title:\")\n",
        "  books.append(title)\n",
        "print(\"Book List:\")\n",
        "for b in books:\n",
        "  print(b)\n",
        "search=input(\"Enter book title to search:\")\n",
        "if search in books:\n",
        "  print(\"Book found\")\n",
        "else:\n",
        "  print(\"Book not found\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EExgs4LIMnBp",
        "outputId": "5ab82ec6-ab36-4aa4-8a9d-49d7ca9128a2"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Book List Operations\n",
            "Enter book title:R\n",
            "Enter book title:c\n",
            "Enter book title:c++\n",
            "Book List:\n",
            "R\n",
            "c\n",
            "c++\n",
            "Enter book title to search:python\n",
            "Book not found\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Word Frequency Count\")\n",
        "sentence=input(\"Enter a sentence:\")\n",
        "words=sentence.split()\n",
        "for word in set(words):\n",
        "  print(word,\":\",words.count(word))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c1GAxv5BNlKh",
        "outputId": "155632f4-0479-43e8-96c7-38f119bbde35"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Word Frequency Count\n",
            "Enter a sentence:but but i am in hurry\n",
            "hurry : 1\n",
            "in : 1\n",
            "i : 1\n",
            "am : 1\n",
            "but : 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Stack Operations\")\n",
        "\n",
        "stack=[]\n",
        "\n",
        "stack.append(10)\n",
        "stack.append(20)\n",
        "stack.append(30)\n",
        "\n",
        "print(\"Stack after push:\",stack)\n",
        "\n",
        "item =stack.pop()\n",
        "\n",
        "print(\"Deleted element:\",item)\n",
        "print(\"Stack after pop:\",stack)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bpBznG_lOfA1",
        "outputId": "76c786ad-d8b4-4ad9-cff6-7e14415e456b"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Stack Operations\n",
            "Stack after push: [10, 20, 30]\n",
            "Deleted element: 30\n",
            "Stack after pop: [10, 20]\n"
          ]
        }
      ]
    }
  ]
}
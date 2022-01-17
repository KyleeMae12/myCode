//this is based off the game hangman
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int index = 0;
    int lives = 6;

    Data d = new Data();

    String answerWord = d.getRandomWord();
    final String originalAnswerWord = answerWord;
    String userWord = "";
    String userInput;
    String hangman = "   ______\n   |    |\n   |    *\n   |   *~*\n   |   **\n___|_______\n";
    String hangmanPrint = hangman.replace("*", " ").replace("~", "");
    ArrayList<String> guessedLetters = new ArrayList<String>();
    ArrayList<String> guessedIncorrectLetters = new ArrayList<String>();
    boolean oneIncorrect = false;
    boolean alreadyGuessed = false;

    for (int i = 0; i < answerWord.length(); i++) {
      if (answerWord.substring(i,i+1).equals(" ")) {
        userWord += " ";
      } else {
      userWord += "_";
      }
    }

    while (lives > 0 && userWord.indexOf("_") > -1) {
      System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
      if (alreadyGuessed) {
        System.out.println("You have already guessed that letter");
        alreadyGuessed = false;
      }
      System.out.println("Lives: " + lives);
      if (oneIncorrect) {
        System.out.println("Incorrect guesses: " + guessedIncorrectLetters.toString().replace("[","").replace("]",""));
      }
      System.out.println(hangmanPrint);
      System.out.println("This is your word:" + userWord);
      userInput = sc.nextLine();
      index = answerWord.indexOf(userInput);
      if (guessedLetters.contains(userInput)) {
        alreadyGuessed = true;
      } else if (index > -1) {
        guessedLetters.add(userInput);
        while (index > -1) {
          userWord = userWord.substring(0,index) + userInput + userWord.substring(index+1);
          answerWord = answerWord.substring(0,index) + "_" + answerWord.substring(index+1);
          index = answerWord.indexOf(userInput);
        }
      } else {
        lives--;
        guessedLetters.add(userInput);
        guessedIncorrectLetters.add(userInput);
        Collections.sort(guessedIncorrectLetters);
        oneIncorrect = true;
        hangman = getHangman(lives, hangman);
        hangmanPrint = hangman.replace("*", " ").replace("~", "");
      }
    }


    System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    System.out.println("Lives: " + lives);
    System.out.println("Incorrect guesses: " + guessedIncorrectLetters.toString().replace("[","").replace("]",""));
    System.out.println(hangmanPrint);
    System.out.println("The word: " + originalAnswerWord);
    System.out.println("Your word: " + userWord);

    if (originalAnswerWord.equals(userWord)) {
      System.out.println("You win!!");
    } else {
      System.out.println("You lose! :(");
    }
    sc.close();
  }
  
  public static String getHangman(int number, String hangmanBody) {
    if (number == 5) {
      return hangmanBody = hangmanBody.substring(0,hangmanBody.indexOf("*")) + "o" + hangmanBody.substring(hangmanBody.indexOf("*")+ 1);
    } else if (number == 3 || number == 1) {
      return hangmanBody = hangmanBody.substring(0,hangmanBody.indexOf("*")) + "/" + hangmanBody.substring(hangmanBody.indexOf("*")+ 1);
    } else if (number == 4) {
      return hangmanBody = hangmanBody.substring(0,hangmanBody.indexOf("~")) + "|" + hangmanBody.substring(hangmanBody.indexOf("*")+ 1);
    } else {
      return hangmanBody = hangmanBody.substring(0,hangmanBody.indexOf("*")) + "\\" + hangmanBody.substring(hangmanBody.indexOf("*")+ 1);
    }
  }
  
}

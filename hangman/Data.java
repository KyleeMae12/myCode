import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Data {
  private ArrayList<String> words = new ArrayList<String>();

  public Data() {
    readData();
  }

  public void readData() {
    String line = "";
    
    try {
      BufferedReader br = new BufferedReader(new FileReader("Words.txt"));
      while ((line = br.readLine()) != null) {
        words.add(line);
      }
      br.close();

    }
    
    catch(IOException e) {
      e.printStackTrace();
    }
  }

  public String getRandomWord() {
    int randomIndex = (int) (Math.random()*(words.size()));
    return words.get(randomIndex);
  }
  
}

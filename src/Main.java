import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Haffman haffman = new Haffman();
        haffman.encode(readFile("src/file.txt").toLowerCase());
    }

    public static String readFile(String path) {
        StringBuilder str = new StringBuilder();
        try (Scanner scan = new Scanner(new FileReader(path))) {
            while (scan.hasNext())
                str.append(scan.nextLine()).append("\n");
            return str.toString();
        } catch (FileNotFoundException e) {
            System.err.println("File not found(");
        }
        return null;
    }
}
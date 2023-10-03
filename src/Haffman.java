import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Haffman {
    private HaffmanNode node, root;

    public Haffman() {
        root = null;
    }

    public void encode(String text) {
        Map<String, Integer> map = getCodes(text);
        PriorityQueue<HaffmanNode> priorityQueue = new PriorityQueue<>((HaffmanNode a, HaffmanNode b) ->
                Integer.compare(a.getFrequency(), b.getFrequency()));
        for (Map.Entry<String, Integer> entry : map.entrySet())
            priorityQueue.add(new HaffmanNode(entry.getValue(), entry.getKey()));

        while (priorityQueue.size() > 1) {
            HaffmanNode a = priorityQueue.poll();
            HaffmanNode b = priorityQueue.poll();

            HaffmanNode c = new HaffmanNode(a.getFrequency() + b.getFrequency(), "-");
            c.setLeft(a);
            c.setRight(b);

            priorityQueue.add(c);
        }

        HaffmanNode root = priorityQueue.poll();
        Map<String, String> codesMap = new HashMap<>();
        printCodes(root, "", codesMap);
        writeFile("D:\\LABS\\АСД\\codes.txt", codesMap);

        StringBuilder encodedString = new StringBuilder();
        for (int i = 0; i < text.length(); i++)
            encodedString.append(codesMap.get(String.valueOf(text.charAt(i))));

        System.out.println("coded: " + encodedString);
        writeFile("D:\\LABS\\АСД\\str.txt", encodedString.toString());
    }

    private void writeFile(String path, Map<String, String> map) {
        try (FileWriter writer = new FileWriter(path)) {
            Set<String> keys = map.keySet();
            for (String key : keys) {
                char s = map.get(key).charAt(0);
                String t = Integer.toHexString(s);
//                writer.write(Integer.toHexString(key.charAt(0)) + " " + map.get(key) + "\n");
                writer.write(key.charAt(0) + " " + map.get(key) + "\n");
            }
        } catch (IOException e) {
            System.err.println("File not found(");
        }
    }

    private void writeFile(String path, String str) {
        try (FileWriter writer = new FileWriter(path)) {
            writer.write(str);
        } catch (IOException e) {
            System.err.println("File not found(");
        }
    }

    public static void printCodes(HaffmanNode root, String code, Map<String, String> codesMap) {
        if (root == null)
            return;

        if (root.getLeft() == null && root.getRight() == null)
            codesMap.put(root.getEl(), code);

        printCodes(root.getLeft(), code + "0", codesMap);
        printCodes(root.getRight(), code + "1", codesMap);
    }

    private Map<String, Integer> getCodes(String text) {
        String[] alphabet = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с",
                "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", ",", ".", "?", "!", ":", ";", "1", "2",
                "3", "4", "5", "6", "7", "8", "9", "0", " ", ")", "(", "/", "-", "–", "\n"};
        Matcher matcher;
        Map<String, Integer> map = new HashMap<>();
        int count = 0;
        for (String s : alphabet) {
            matcher = Pattern.compile("[" + s.toLowerCase() + "]").matcher(text);
            while (matcher.find())
                count++;
            if (count != 0) {
                map.put(s, count);
            }
            count = 0;
        }
        return map;
    }
}

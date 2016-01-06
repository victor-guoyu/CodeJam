import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class T9 {

	private static String [] keyPad = {" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

	private static String parseT9(String input) {
		StringBuilder sb = new StringBuilder();
		int previousKey = -1;
		for (int i = 0; i < input.length(); i++) {
			char c = input.charAt(i);
			for (int currentKey = 0; currentKey < keyPad.length; currentKey++) {
				int charPos = keyPad[currentKey].indexOf(c);
				if (charPos >=0) {
					if (currentKey == previousKey) {
						sb.append(keyPad[0]);
					}
					int repeatTimes = charPos +1;
					for (int k = 0; k < repeatTimes; k++) {
						sb.append(currentKey);
					}
					previousKey = currentKey;
				}
			}
		}
		return sb.toString();
	}

	public static void main(String [] args) {
		String fileName = "C-small-practice.in";
		try {
			FileReader fileReader = new FileReader(fileName);
			BufferedReader reader = new BufferedReader(fileReader);
			int numberOfCases = Integer.parseInt(reader.readLine());
			for (int i = 0; i < numberOfCases; i++) {
				String result = parseT9(reader.readLine());
				System.out.println(String.format("Case #%s: %s", i+1, result));
			}
			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}

import java.io.*;

public class ReverseWords {

	public static void main(String[] args) {
		String fileName = "B-large-practice.in";
		try {
			FileReader fileReader= new FileReader(fileName);
			BufferedReader reader = new BufferedReader(fileReader);
			int numberOfCases = Integer.parseInt(reader.readLine());
			for (int i = 0; i < numberOfCases; i++) {
				String[] words = reader.readLine().split("\\s+");
				StringBuilder sb = new StringBuilder();
				sb.append(words[words.length -1]);
				for (int j = words.length - 2; j >= 0; j--) {
					sb.append(" ");
					sb.append(words[j]);
				}
				System.out.println(String.format("Case #%s: %s", i+1, sb.toString()));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}

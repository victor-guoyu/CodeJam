import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class StoreCredit {
	private static class DataSet {
		final int caseNumber;
		final int credit;
		final int[] items;

		public DataSet(int caseNumber, int credit, int[] items) {
			this.caseNumber = caseNumber;
			this.credit = credit;
			this.items = items;
		}
	}

	public static void main(String[] args) {
		String fileName = "A-small-practice.in";
		try {
			FileReader fr = new FileReader(fileName);
			BufferedReader bufferedReader = new BufferedReader(fr);
			int numberOfCases = Integer.parseInt(bufferedReader.readLine());
			for (int i = 0; i < numberOfCases; i++) {
				int credit = Integer.parseInt(bufferedReader.readLine());
				int numberOfItems = Integer.parseInt(bufferedReader.readLine());
				String[] pricesToParse = bufferedReader.readLine().split("\\s+");
				int[] prices = new int[numberOfItems];
				for (int j = 0; j < numberOfItems; j++) {
					prices[j] = Integer.parseInt(pricesToParse[j]);
				}
				DataSet dataSet = new DataSet(i+1, credit, prices);
				findSolution(dataSet);
			}
			bufferedReader.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static void findSolution(DataSet dataSet) {
		int bestFirstPost = -1;
		int bestSecondPost = -1;
		int maxCombinedPrice = 0;
		for (int firstPos = 0; firstPos < dataSet.items.length - 1; firstPos++) {
			for (int secondPos = firstPos+1; secondPos < dataSet.items.length; secondPos++) {
				int currentPrice = dataSet.items[firstPos] + dataSet.items[secondPos];
				if (currentPrice > maxCombinedPrice && currentPrice <= dataSet.credit) {
					maxCombinedPrice = currentPrice;
					bestFirstPost = firstPos;
					bestSecondPost = secondPos;
				}
			}
		}
		System.out.println(String.format("Case #%s: %s %s", dataSet.caseNumber, bestFirstPost+1, bestSecondPost+1));
	}

}

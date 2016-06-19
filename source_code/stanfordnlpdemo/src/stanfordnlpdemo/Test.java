// CIS 700 Term Project
// Saurabh Patel, Ojas Juneja, Ronak Bhuptani

package stanfordnlpdemo;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Test {

	public static void main(String[] args) {
		try {
			ArrayList<String> filesList = new ArrayList<String>();
			
			//filesList.add("BeforeIWake.txt");
			//filesList.add("CriminalMovie.txt");
			//filesList.add("Demolition.txt");
			//filesList.add("ElvisAndNixon.txt");
			//filesList.add("FanTheFilm.txt");
			//filesList.add("GreenRoomMovie.txt");
			//filesList.add("HardcoreHenry.txt");
			//filesList.add("JungleBook.txt");
			//filesList.add("LouderThanBombs.txt");
			//filesList.add("TheHuntsman.txt");
			//filesList.add("TheManWhoKnewInfinity.txt");
			filesList.add("AHologramForTheKing.txt");
			
		
			for (int i = 0; i < filesList.size(); i++) {
				String filename = filesList.get(i);
				readFile1(filename);
			}
			
			
		} catch (IOException e) {
			System.out.println("Exception : " + e.getMessage());
			e.printStackTrace();
		}
	}

	private static void readFile1(String filename) throws IOException {
		File fin = new File(filename);
		int p = 0,n = 0,ne = 0;
		String[] sentimentText = { "Very Negative", "Negative", "Neutral", "Positive", "Very Positive" };
		File fout = new File(filename+".output");
		FileOutputStream fos = new FileOutputStream(fout);
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));

		NLP.init();
		FileInputStream fis = new FileInputStream(fin);
		// Construct BufferedReader from InputStreamReader
		BufferedReader br = new BufferedReader(new InputStreamReader(fis));
		String line = null;
		System.out.println("started : "+filename);
		while ((line = br.readLine()) != null) {
			int senti = NLP.findSentiment(line.trim());
			StringBuilder sb = new StringBuilder();
			//System.out.println(line);
			if (senti == 0 || senti == 1) {
				n++;
				sb.append(String.valueOf(0)); // + "\t" + line);

			} else if (senti == 2) {
				ne++;
				sb.append(String.valueOf(-1)); // + "\t" + line);
			} else if (senti == 3 || senti == 4) {
				p++;
				sb.append(String.valueOf(1)); //+ "\t" + line);
			}
			bw.write(sb.toString());
			//System.out.println(sb.toString());
			bw.newLine();
		}
		String s = filename + " : Positive : "+p + " Negative : "+n +" Neutral "+ne;
		bw.write(String.valueOf(s));
		br.close();
		bw.close();
		System.out.println(filename + " : Positive : "+p + " Negative : "+n +" Neutral "+ne);
	}
}
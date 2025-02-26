import java.math.BigInteger;
import java.util.Scanner;

public class hasher {
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		System.out.println("Compute an 8-byte integer hash!");
		System.out.print("Enter your string: ");
		String input = console.nextLine();
		long hash = computeHash(input);
		System.out.println("Your hash is " + String.valueOf(hash));
		console.close();
	}

	public static long computeHash(String input) {
		// Add salt to input
		String saltedInput = "a_pad{" + input + "}random-bit";

		// Compute hash
		BigInteger result = new BigInteger("49");
		for (int charId = 0; charId < saltedInput.length(); charId++) {
			int codePoint = Character.codePointAt(saltedInput, charId);
			result = result.modPow(bigPrime, expoMod);
			result = result.add(deltaAdd);
			result = result.add(BigInteger.valueOf(codePoint).modPow(bigPrime, expoMod));
		}
		result = result.mod(resultMod);

		// Return result
		return result.longValue();
	}

	// Hash configs
	private static final BigInteger resultMod = new BigInteger("2").pow(64);
	private static final BigInteger expoMod = new BigInteger("68445073147145418392650232728550764697530913594510623851220659487818545791981");
	private static final BigInteger bigPrime = new BigInteger("276778552634165860666436318555312156587");
	private static final BigInteger deltaAdd = new BigInteger("87");
}

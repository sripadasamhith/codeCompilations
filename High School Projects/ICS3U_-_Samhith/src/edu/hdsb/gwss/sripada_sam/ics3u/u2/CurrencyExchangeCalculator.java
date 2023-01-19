/*
NAME: SAMHITH SRIAPDA
DATE: MARCH 6, 2018
PURPOSE: TO CONVERT THE PRICE OF AN ITEM IN US DOLLARS INTO A FOREIGN 
         CURRENCY RATE
        EX. CAD -> USD
 */
package edu.hdsb.gwss.sripada_sam.ics3u.u2;

import java.util.Scanner;

/**
 *
 * @author Samhith
 */
public class CurrencyExchangeCalculator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here

        // CONSTANTS
        double USD_Rate = 0.77265;
        double EUR_Rate = 0.622094;
        double GBP_Rate = 0.0555884;
        double INR_Rate = 50.146688;
        double AUD_Rate = 0.993222;
        double CAD_Rate = 1;
        double SGD_Rate = 1.018635;

        String USD, EUR, GBP, INR, AUD, CAD, SGD;

        USD = "USD";
        EUR = "EUR";
        GBP = "GBP";
        INR = "INR";
        AUD = "AUD";
        CAD = "CAD";
        SGD = "SGD";
        // RATES ABOVE ARE FROM CAD($) PERSPECTIVE

        // VARIABLES
        String userInput;
        double price;
        double convertedRate = 0.0;
        // OBJECTS

        Scanner input = new Scanner(System.in);

        // INTRO
        System.out.println("Hello! We are converting currency rates, your options are:\nCAD\nAUD\nSGD\nUSD\nEUR\nGBP\nINR");

        // INPUT
        System.out.println("Please enter the currency of which you would like to convert to from the options above: ");
        userInput = input.nextLine();

        System.out.println("Please enter the price of your item in Canadian Dollars: ");
        price = input.nextDouble();

        // PROCESSING
        if (userInput.equals( "USD") ) {
            convertedRate = price * USD_Rate;
        } else if (userInput == "EUR") {
            convertedRate = price * EUR_Rate;
        } else if (userInput == "GBP") {
            convertedRate = price * GBP_Rate;
        } else if (userInput == "INR") {
            convertedRate = price * INR_Rate;
        } else if (userInput == "AUD") {
            convertedRate = price * AUD_Rate;
        } else if (userInput == "SGD") {
            convertedRate = price * SGD_Rate;
        }
        // OUTPUT

        System.out.println("Great! your price in " + userInput + " is " + convertedRate);

    }

}

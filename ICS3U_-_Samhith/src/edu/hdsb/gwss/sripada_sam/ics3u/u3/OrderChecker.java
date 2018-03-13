/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.hdsb.gwss.sripada_sam.ics3u.u3;

import java.text.NumberFormat;
import java.util.Scanner;

/**
 *
 * @author Samhith
 */
public class OrderChecker {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here

        // Constants
        final double BOLT_PRICE = 0.05;
        final double NUT_PRICE = 0.03;
        final double WASHER_PRICE = 0.01;

        Scanner input = new Scanner(System.in);
        NumberFormat money = NumberFormat.getCurrencyInstance();

        // Variables
        int bolts, nuts, washers;
        double total;

        String statusNB = "";
        String statusWashers = "";

        // Input
        System.out.println("Number of Bolts: ");
        bolts = input.nextInt();

        System.out.println("Number of Nuts: ");
        nuts = input.nextInt();

        System.out.println("Number of Washers: ");
        washers = input.nextInt();

        // Processing
        total = bolts * BOLT_PRICE + nuts * NUT_PRICE + washers * WASHER_PRICE;

        if (bolts == nuts && 2 * bolts == washers) {

            statusNB = "Order is error free!";

        } else if (bolts > nuts) {

            statusNB = "Too few nuts";

        } else {

            statusNB = "Too few bolts";

        }
        if (bolts * 2 != washers) {

            statusWashers = "Too few washers";
            // \n%13s

        }

        // Output
        // System.out.println("\nCheck Order: " + statusNB + "\nTotal Cost: " + money.format(total));
        System.out.format("%-20s %20s", "Number of Bolts:", bolts + "\n");
        System.out.format("%-20s %20s", "Number of Nuts:", nuts + "\n");
        System.out.format("%-20s %20s", "Number of Washers:", washers + "\n");
        
        if (statusWashers.isEmpty()) {
            
            System.out.format("%-20s %20s", "Check the order:", statusNB + "\n");
            
        } else {
            
            System.out.format("%-20s %20s", "Check the order:", statusNB + "\n");
            System.out.format("%-20s %20s", "                ", statusWashers + "\n");
            
        }
        
        System.out.format("%-20s %20s", "Total Cost:", money.format(total) + "\n");

    }

}

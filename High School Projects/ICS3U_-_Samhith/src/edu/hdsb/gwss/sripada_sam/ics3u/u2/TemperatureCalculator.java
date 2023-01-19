/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.hdsb.gwss.sripada_sam.ics3u.u2;

import java.util.Scanner;

/**
 *
 * @author 1sripadasam
 */
public class TemperatureCalculator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here

        Scanner input = new Scanner(System.in);

        double celcius;
        double fTemp;

        System.out.println("Enter a celcius tmperature value: ");

        celcius = input.nextDouble();

        fTemp = celcius * 1.8 + 32;

        System.out.println("The temperature in F is " + fTemp);

    }

}

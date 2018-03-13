/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.hdsb.gwss.sripada_sam.ics3u.u1;

/**
 *
 * @author 1SRIPADASAM
 */
public class OlympicMedalCount {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        //Table
        
        System.out.println("Countries   Gold    Silver  Bronze  Total   PG(%)");
        System.out.println("Canada      3       4       3       10      30.0");
        System.out.println("USA         3       1       2       6       50.0");
        System.out.println("France      2       1       2       5       40.0");
        System.out.println("Norway      3       5       5       11      27.3");
        System.out.println("Netherlands 4       4       2       10      40.0");
        System.out.println("Germany     5       2       2       9       55.6");
        
        
        // New Table
        
        System.out.format("%15s | %4s | %6s | %6s | %5s | %5s |\n", "Countries", "Gold", "Silver", "Bronze", "Total", "PG(%)");
        System.out.format("%15s | %4s | %6s | %6s | %5s | %5s |\n", "Canada", 3, 4, 3, 10, 30.0);
        System.out.format("%15s | %4s | %6s | %6s | %5s | %5s |\n", "USA", 3, 1, 2, 6, 50.0);
        System.out.format("%15s | %4s | %6s | %6s | %5s | %5s |\n", "France", 2, 1, 2, 5, 40.0);
        System.out.format("%15s | %4s | %6s | %6s | %5s | %5s |\n", "Norway", 3, 5, 5, 11, 27.3);
        System.out.format("%15s | %4s | %6s | %6s | %5s | %5s |\n", "Netherlands", 4, 4, 2, 10, 40.0);
        System.out.format("%15s | %4s | %6s | %6s | %5s | %5s |\n", "Germany", 5, 2, 2, 9, 55.6);
    }
    
}

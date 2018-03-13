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
public class CellSell {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Scanner input = new Scanner(System.in);
        NumberFormat money = NumberFormat.getCurrencyInstance();
        
        double userDaytimeMin = 0, userEveningMin = 0, userWeekendMin = 0;
        double costPlanA, costPlanB;
        String cheaperPlan = "";
        boolean isSamePrice = false;
        
        double PLAN_A_DAYTIME_MIN = 0; 
        double PLAN_A_EVENING_MIN = 0;
        double PLAN_A_WEEKEND_MIN = 0;
        
        double PLAN_B_DAYTIME_MIN = 0;
        double PLAN_B_EVENING_MIN = 0;
        double PLAN_B_WEEKEND_MIN = 0;
        
        System.out.println("Number of Daytime Minutes: ");
        userDaytimeMin = input.nextDouble();
        
        System.out.println("Number of Evening Minutes: ");
        userEveningMin = input.nextDouble();
        
        System.out.println("Number of Weekend Minutes: ");
        userWeekendMin = input.nextDouble();
        
        if (userDaytimeMin > 100) {
            
            PLAN_A_DAYTIME_MIN = (userDaytimeMin - 100) * 0.25;
            
        } else {
            
            PLAN_A_DAYTIME_MIN = 0;
            
        }
        
        PLAN_A_EVENING_MIN = userEveningMin * 0.15;
        PLAN_A_WEEKEND_MIN = userWeekendMin * 0.20;
        costPlanA = PLAN_A_DAYTIME_MIN + PLAN_A_EVENING_MIN + PLAN_A_WEEKEND_MIN;
        
        if (userDaytimeMin > 250) {
            
            PLAN_B_DAYTIME_MIN = (userDaytimeMin - 250) * 0.45;
            
        } else {
            
            PLAN_B_DAYTIME_MIN = 0;
            
        }
        
        PLAN_B_EVENING_MIN = userEveningMin * 0.35;
        PLAN_B_WEEKEND_MIN = userWeekendMin * 0.25;
        costPlanB = PLAN_B_DAYTIME_MIN + PLAN_B_EVENING_MIN + PLAN_B_WEEKEND_MIN;
        
        
        if (isSamePrice = true) {
            
            cheaperPlan = "Both Plan A and B are the same price";
            
        } else {
            
            cheaperPlan = costPlanA > costPlanB ? "Plan B is cheaper" : "Plan A is cheaper";
            
        }
        
        if (costPlanA == costPlanB) {
            
            isSamePrice = true;
            
        }
        
        System.out.println("Plan A costs " + money.format(costPlanA));
        System.out.println("Plan B costs " + money.format(costPlanB));
        System.out.println(cheaperPlan);
        
    }
    
}

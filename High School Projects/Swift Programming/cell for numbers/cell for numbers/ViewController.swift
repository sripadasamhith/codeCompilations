//
//  ViewController.swift
//  cell for numbers
//
//  Created by Samhith Sripada on 2017-12-23.
//  Copyright © 2017 HackedApple. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    @IBOutlet weak var tableView: UITableView!
    
    
    
    let cellContent = 1 ... 50

    internal func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    
        return cellContent.count
    
    }
    
    

    internal func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        var cell = UITableViewCell(style: UITableViewCellStyle.default, reuseIdentifier: "prototypeCell")
        
        cell.textLabel?.text = String(indexPath.row + 1)
        
        return cell
    }

    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}


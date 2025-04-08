def purchase_item(price, gold_available):
    if price> gold_available:
            raise Exception("not enough gold")
        
    else:
        left_over = gold_available - price
        return left_over
        

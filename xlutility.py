import xlrd, xlwt, openpyxl


def GetCellVal(file_path, sht_name, cell_row, cell_col):
    """
        This function returns the cell content of an excel worksheet
    """
    wb  = xlrd.open_workbook(file_path) # open workbook
    sht = wb.sheet_by_name(sht_name)    # activate worksheet
    val = sht.cell(cell_row-1, cell_col-1).value
    return val

	
def GetCellValForRange(file_path, sht_name, cell_row, cell_col, rangeNo=1):
    """
        This function returns the cell content of an excel worksheet
		
    """
    #wb  = xlrd.open_workbook(file_path) # open workbook
    #sht = wb.sheet_by_name(sht_name)    # activate worksheet
    rangeValData = []			# data for range holder
    for x in range(rangeNo):
        rangeValData.append(GetCellVal(file_path, sht_name, cell_row+x, cell_col))
        
    return rangeValData




def OpenWbActivateWs(file_path, sht_name):
    wb  = xlrd.open_workbook(file_path) # open workbook
    sht = wb.sheet_by_name(sht_name)    # activate worksheet
    return sht



def GetEmptyCellRowNo(file_path, sht_name, col_no=1, start_row=1):
    """
        This function returns the next available row cell
        In other words, the end of data in row.
    """
    #wb_sht = OpenWbActivateWs(file_path, sht_name)
    data = []
    #start_row = start_row-1
    try:
        while True:
            data.append(GetCellVal(file_path, sht_name, start_row, col_no))
            #print(start_row, data[-1])              # debug
            
            if len(data) > 2:                       # at least 2 values in list
                data = data[-2:]                    # retain last values in data list
                
            if data.count("") == 2: break

            start_row += 1
        
        return start_row-len(data)
    
    except(IndexError):
         return start_row





def SetCellVal(file_path, sht_name, cell_row, cell_col, val):
    """
        This function input content into an excel worksheet cell
    """
    wb_sht = OpenWbActivateWs(file_path, sht_name)
    #wb  = xlrd.open_workbook(file_path) # open workbook
    #sht = wb.sheet_by_name(sht_name)    # activate worksheet
    wb_sht.cell(cell_row-1, cell_col-1).value = val
    #return val     

    
if __name__ == "__main__":
    pass

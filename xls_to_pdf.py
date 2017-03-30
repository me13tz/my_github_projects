import win32com.client

o = win32com.client.Dispatch("Excel.Application")

o.Visible = False

wb_path = r'C:\Users\ProfileName\Documents\SpreadSheetName.xlsx'  #Path to your spreadsheet/workbook

wb = o.Workbooks.Open(wb_path)



ws_index_list = ["sheet1","sheet2", "sheet3", "sheet4"] # List of sheets you wanna print


for worksheet in ws_index_list:
    path_to_pdf = r'C:\Users\ProfileName\Documents\SomeFolder\{}.pdf'.format(str(worksheet))
    print(path_to_pdf)

    wb.WorkSheets(worksheet).Select()

    wb.ActiveSheet.ExportAsFixedFormat(0, path_to_pdf)


print("Done.")
import pandas as pd


def column_extraction(fpath):
    df = pd.read_csv(fpath, usecols = ["comment"])
    df.to_csv("arabic_" + fpath.split(".")[0] + ".csv", index = False)
    df_all_data = pd.read_csv(fpath)
    print(df_all_data.dtypes)
    print(df_all_data.columns)
    print(df_all_data.head())
    imp_cols = list(df_all_data.columns)
    imp_cols.remove("comment")
    return imp_cols, list(df_all_data.columns).index("comment")






needed_cols, arabic_comments_index = column_extraction("comments_art-et-culture.csv")
print(needed_cols)
print(arabic_comments_index)
print("-"*50)






def csv_to_txt(fcsv):
    ftxt = fcsv.split(".")[0] + ".txt"
    with open(fcsv, "r") as cv, open(ftxt, "w") as tx:
        content = cv.read()
        tx.write(content)

csv_to_txt("arabic_comments_art-et-culture.csv")






def adding_arabic_comments(fpath_all_data, fpath_needed_cols, fpath_arabic_comments, add_col_index):
    df_data = pd.read_csv(fpath_all_data, usecols = fpath_needed_cols)
    df_arabic_comments = pd.read_csv(fpath_arabic_comments)
    clean_str = [string.strip("'") for lst in df_arabic_comments.values.tolist() for string in lst]

    df_data.insert(loc = add_col_index,
                    column = df_arabic_comments.columns[0],
                    value = clean_str)
    # print("col_name:", df_arabic_comments.columns[0])
    # print(df_arabic_comments.values.tolist())
    # df_data.to_csv("all_data.csv", index = False)    ### shows arabic text with the same problem it was (symbolic text)
    df_data.to_excel(fpath_all_data.split(".")[0] + ".xlsx", index = False)

    print(df_data.columns)
    print(df_data.head())
    print(df_arabic_comments.head())

adding_arabic_comments("comments_art-et-culture.csv", needed_cols, "arabic_comments_art-et-culture.txt", arabic_comments_index)






def excel_to_csv(fexcel):
    df = pd.read_excel(fexcel)
    df.to_csv(fexcel.split(".")[0] + "__.csv")

excel_to_csv("comments_art-et-culture.xlsx")

import matplotlib.pyplot as plt
def show_by_plot(plt,data,label,color,linewidth,start_date,end_date,title):
    # 可视化结果
    print(data.iloc[5])
    plt.figure(figsize=(20, 10))   #画布的大小
    plt.plot(data["close"], label='Close Price', color='blue',linewidth=linewidth)

    # plt.plot(result.loc[result['Signal'] == 1].index,
    #           result['Short_MA'][result['Signal'] == 1],
    #           '^', markersize=10, color='g', lw=0, label='Buy Signal')
    # plt.plot(result.loc[result['Signal'] == -1].index,
    #           result['Short_MA'][result['Signal'] == -1],
    #           'v', markersize=10, color='r', lw=0, label='Sell Signal')
    plt.subplots_adjust(left=0.03, right=0.995, bottom=0.04, top=0.97)
    plt.xlim(start_date,end_date)
    plt.grid(True, axis='both', color='grey', linestyle='--', linewidth=0.5)
    plt.title(title)
    plt.legend()
    plt.show()
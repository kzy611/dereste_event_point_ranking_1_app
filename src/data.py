import pandas as pd
import matplotlib.pyplot as plt

from selection import Selections, Selection
from utils import execute_dict_functions
from inputs import (input_yes_no, input_date, input_str, input_natural_number,
                    input_positive_number)

# データのインプットに使う
def input_event_data():
    # カラム名: 入力に使う関数
    in_dict = {
        'date':       input_date,
        'event_name': input_str,
        'point':      input_natural_number,
        'length(h)':  input_positive_number,
    }
    return execute_dict_functions(in_dict)

# データフレームを管理するクラス
class DataFrame:
    def __init__(self, file_info):
        # グラフ表示設定
        self.plot_params = ['point', 'length(h)'] # 表示項目
        # ファイル読み込み
        self.paths = file_info['paths']
        self.files = file_info['files']
        self.df = self.load_dataframe(self.path_dataframe)
    
    # データフレームファイルのパス
    @property
    def path_dataframe(self):
        return self.paths['data'] + self.files['dataframe']
    
    # データ読み込み
    def load_dataframe(self, path):
        df = pd.read_csv(path)
        df['date'] = pd.to_datetime(df['date']).dt.date
        df.set_index('date', inplace=True)
        return df
    
    # データ更新
    def update_dataframe(self):
        self.df.to_csv(self.path_dataframe)
    
    # 選択肢
    def select_method(self):
        selections = Selections([
            Selection(
                name = 'データフレーム表示',
                method = self.show_dataframe,
            ),
            Selection(
                name = 'グラフ表示',
                method = self.show_graph,
            ),
            Selection(
                name = 'データ追加',
                method = self.add_data,
            ),
            Selection(
                name = 'データ削除',
                method = self.delete_data,
            ),
        ])
        selections.select_method()
    
    # データフレーム表示
    def show_dataframe(self):
        print(self.df)
    
    # グラフ表示
    def show_graph(self):
        for key in self.plot_params:
            print(key)
            self.df[key].plot()
            plt.title(key)
            plt.show()
    
    # データ追加
    def add_data(self):
        data_dict = input_event_data()
        # Noneが帰ってきたらキャンセル
        if data_dict is None:
            return
        df_add = pd.DataFrame(data_dict, index=['0']).set_index('date')
        # 既存のデータフレームに追加
        self.df = pd.concat([self.df, df_add], axis=0).sort_index()
        self.update_dataframe()
    
    # データ削除
    def delete_data(self):
        print('削除するデータの日付を指定してください')
        date = input_date()
        # Noneが帰ってきたらキャンセル
        if date is None:
            return
        # 入力チェック
        try:
            df_del = self.df.loc[[date], :]
        except KeyError:
            print('一致するイベントがありません')
            return
        # 最終確認
        print('以下のイベントを削除して良いですか？')
        print(df_del)
        del_flg = input_yes_no()
        if del_flg:
            # 削除
            self.df.drop(index=date, inplace=True)
            # 保存
            self.update_dataframe()
            print('削除しました')
        else:
            print('キャンセルします')
    
    # データフレーム渡す
    def get_dataframe(self):
        return self.df

if __name__ == '__main__':
    import config
    data_frame = DataFrame(config.file_info)
    data_frame.select_method()

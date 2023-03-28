import pandas as pd
from otlang.sdk.syntax import Keyword, OTLType, Subsearch
from pp_exec_env.base_command import BaseCommand, Syntax


class MapcolumnsCommand(BaseCommand):
    # define syntax of your command here
    syntax = Syntax(
        [
            Subsearch("mapping_df", required=True),
            Keyword("source", required=False, otl_type=OTLType.TEXT),
            Keyword("target", required=False, otl_type=OTLType.TEXT)
        ],
    )
    use_timewindow = False  # Does not require time window arguments
    idempotent = True  # Does not invalidate cache

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.log_progress('Start mapcolumns command')

        mapping_df = self.get_arg("mapping_df").value
        source = self.get_arg('source').value or 'metric_name'

        target = self.get_arg('target').value or 'metric_long_name'
        try:
            mapping_dict = dict(zip(mapping_df[source], mapping_df[target]))
            df = df.rename(columns=mapping_dict)
        except KeyError:
            self.logger.error('Given columns names {first} or {second} are not in the subsearch results!'
                              .format(first=source, second=target))

        self.log_progress('End mapcolumns command')
        return df

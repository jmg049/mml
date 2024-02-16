from typing import Dict, Any, Union, Tuple

import pandas as pd


_backend = "python"
_console = None


def set_backend(backend):
    assert backend in ["python", "rich"]
    global _backend

    if backend == "rich":
        try:
            global rich
            global _console

            import rich
            from rich.console import Console
        except ImportError:
            raise ImportError(
                "rich is not installed. Please install it using `pip install rich`"
            )
        _console = Console()

    _backend = backend


def box_print(
    header: str,
    *,
    key_colour: str = "bold white",
    value_colour: str = "green",
    header_align: str = "center",
    style="rule.line",
    **kwargs,
):
    global _backend, _console
    if _backend == "python":
        print(f"== {header} ==")
        for k, v in kwargs.items():
            print(f"{k}: {v}")
        print()
    elif _backend == "rich":
        _console.rule(header, style=style, align=header_align)
        for k, v in kwargs.items():
            _console.print(f"[{key_colour}]{k}:[/{key_colour}] [{value_colour}]{v}")


def _split_dict(d: Dict, predicate: callable) -> Tuple[Dict, Dict]:
    return {k: v for k, v in d.items() if predicate(k)}, {
        k: v for k, v in d.items() if not predicate(k)
    }


def handle_metrics(
    metrics: Dict[str, Any],
    format: str,
    row_name: str = "Train",
    print_arrays: bool = False,
) -> Union[None, pd.DataFrame]:
    format = format.lower()
    assert format in [
        "plain",
        "dataframe",
        "markdown",
        "html",
        "json",
        "csv",
        "excel",
        "latex",
        "table",
    ]

    if format == "plain":
        box_print("Metrics", **metrics)
        return None

    else:
        global _backend, _console

        scalars, arrays = _split_dict(metrics, lambda k: isinstance(metrics[k], float))
        df = pd.DataFrame(scalars, index=[row_name])

        if format == "dataframe":
            return df
        elif format == "markdown":
            df_str = df.to_markdown(tablefmt="simple")
        elif format == "table":
            from rich.table import Table
            from rich.align import Align

            table = Table(
                *list(scalars.keys()),
                title=f"{row_name} Metrics",
                highlight=True,
                header_style="bold",
            )
            table.add_row(
                *list(
                    [
                        Align(str(m), vertical="middle", align="right")
                        for m in scalars.values()
                    ]
                )
            )
            df_str = table

        elif format == "html":
            df_str = df.to_html()
        elif format == "json":
            df_str = df.to_json()
        elif format == "csv":
            df_str = df.to_csv()
        elif format == "excel":
            df_str = df.to_excel()
        elif format == "latex":
            df_str = df.to_latex()

        if print_arrays:
            box_print("Metrics", **arrays)

        if _backend == "python":
            print(df_str)
        elif _backend == "rich":

            _console.print(df_str)
        else:
            raise ValueError(f"Invalid format: {format}")


if __name__ == "__main__":
    box_print("Hello, World!", name="John Doe", age=25, city="New York")

    set_backend("rich")
    box_print(
        "Hello, World!", name="John Doe", age=25, city="New York", key_colour="blue"
    )

    metrics = {
        "accuracy": 0.95,
        "precision": 0.96,
        "recall": 0.97,
        "f1": 0.98,
        "roc_auc": 0.99,
        "confusion_matrix": "[[100, 10], [5, 200]]",
    }

    handle_metrics(metrics, "plain")
    handle_metrics(metrics, "table", print_arrays=True)

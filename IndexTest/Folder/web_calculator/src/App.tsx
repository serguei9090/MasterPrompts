import { AnimatePresence, motion } from "framer-motion";
import {
	AlertCircle,
	Calculator as CalcIcon,
	Divide,
	Minus,
	Plus,
	RotateCcw,
	X,
} from "lucide-react";
import type React from "react";
import { useState } from "react";
import { type Operation, useSidecarBridge } from "./hooks/useSidecarBridge";
import "./App.css";

const App: React.FC = () => {
	const [display, setDisplay] = useState("0");
	const [num1, setNum1] = useState<number | null>(null);
	const [operation, setOperation] = useState<Operation | null>(null);
	const [isNewEntry, setIsNewEntry] = useState(true);

	const { calculate, loading, error: apiError } = useSidecarBridge();

	const handleNumber = (n: string) => {
		if (isNewEntry) {
			setDisplay(n);
			setIsNewEntry(false);
		} else {
			setDisplay((prev) => (prev === "0" ? n : prev + n));
		}
	};

	const handleOperation = (op: Operation) => {
		setNum1(parseFloat(display));
		setOperation(op);
		setIsNewEntry(true);
	};

	const handleClear = () => {
		setDisplay("0");
		setNum1(null);
		setOperation(null);
		setIsNewEntry(true);
	};

	const handleCalculate = async () => {
		if (num1 !== null && operation !== null) {
			const currentNum = parseFloat(display);
			const result = await calculate(operation, num1, currentNum);
			if (result !== null) {
				setDisplay(result.toString());
				setNum1(null);
				setOperation(null);
				setIsNewEntry(true);
			}
		}
	};

	const getOpIcon = (op: Operation) => {
		switch (op) {
			case "add":
				return <Plus size={18} />;
			case "sub":
				return <Minus size={18} />;
			case "mul":
				return <X size={18} />;
			case "div":
				return <Divide size={18} />;
		}
	};

	return (
		<div className="container">
			<motion.div
				initial={{ opacity: 0, y: 20 }}
				animate={{ opacity: 1, y: 0 }}
				className="calculator-card glass-panel"
			>
				<header className="calc-header">
					<div className="title-group">
						<CalcIcon className="icon-primary" size={20} />
						<h1>
							LOGIC ENGINE <span className="version">v1.0</span>
						</h1>
					</div>
					<div className="status-indicator">
						<div
							className={`status-dot ${loading ? "status-busy" : "status-ready"}`}
						></div>
						<span className="label-caps">
							{loading ? "PROCESSING" : "READY"}
						</span>
					</div>
				</header>

				<section className="display-area">
					<AnimatePresence mode="wait">
						<motion.div
							key={display}
							initial={{ opacity: 0, x: -10 }}
							animate={{ opacity: 1, x: 0 }}
							exit={{ opacity: 0, x: 10 }}
							className="display-value font-mono"
						>
							{display}
						</motion.div>
					</AnimatePresence>
					<div className="display-meta">
						{num1 !== null && operation !== null && (
							<span className="label-caps active-op">
								{num1} {getOpIcon(operation)}
							</span>
						)}
					</div>
				</section>

				{(apiError || (parseFloat(display) === 0 && operation === "div")) && (
					<motion.div
						initial={{ height: 0, opacity: 0 }}
						animate={{ height: "auto", opacity: 1 }}
						className="error-banner"
					>
						<AlertCircle size={14} />
						<span>{apiError || "SYSTEM FAULT: DIVISION BY ZERO"}</span>
					</motion.div>
				)}

				<div className="keypad">
					<div className="grid-main">
						{["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "."].map(
							(n) => (
								<button
									key={n}
									onClick={() => handleNumber(n)}
									className="btn btn-number glow-hover"
								>
									{n}
								</button>
							),
						)}
						<button onClick={handleClear} className="btn btn-clear glow-hover">
							<RotateCcw size={18} />
						</button>
					</div>

					<div className="grid-ops">
						{(["add", "sub", "mul", "div"] as Operation[]).map((op) => (
							<button
								key={op}
								onClick={() => handleOperation(op)}
								className={`btn btn-op glow-hover ${operation === op ? "btn-op-active" : ""}`}
							>
								{getOpIcon(op)}
							</button>
						))}
						<button
							onClick={handleCalculate}
							className="btn btn-equal glow-hover"
							disabled={loading}
						>
							=
						</button>
					</div>
				</div>
			</motion.div>

			<footer className="footer label-caps">
				Morphic Logic Engine // Tactical Calculator // Sidecar Standard
			</footer>
		</div>
	);
};

export default App;

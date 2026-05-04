import { AnimatePresence, motion } from "framer-motion";
import {
	AlertCircle,
	Calculator as CalcIcon,
	ChevronLeft,
	ChevronRight,
	Divide,
	History as HistoryIcon,
	Minus,
	Percent,
	Plus,
	RotateCcw,
	Ruler,
	Trash2,
	Weight,
	X,
} from "lucide-react";
import type React from "react";
import { useState } from "react";
import { type Operation, useSidecarBridge } from "./hooks/useSidecarBridge";
import "./App.css";

interface HistoryEntry {
	id: string;
	text: string;
}

const App: React.FC = () => {
	const [display, setDisplay] = useState("0");
	const [num1, setNum1] = useState<number | null>(null);
	const [operation, setOperation] = useState<Operation | null>(null);
	const [isNewEntry, setIsNewEntry] = useState(true);
	const [history, setHistory] = useState<HistoryEntry[]>([]);
	const [resultsCount, setResultsCount] = useState(0);
	const [calcMode, setCalcMode] = useState<"math" | "mass" | "distance">(
		"math",
	);
	const [isHistoryOpen, setIsHistoryOpen] = useState(false);

	const LEVEL_REQUIREMENTS = [
		4, 6, 9, 14, 21, 31, 47, 70, 105, 157, 236, 354, 531, 796, 1194, 1791, 2686,
		4029, 6043, 9064,
	];

	const getCurrentLevel = () => {
		let level = 1;
		let cumulative = 0;
		for (let i = 0; i < LEVEL_REQUIREMENTS.length; i++) {
			if (resultsCount >= cumulative + LEVEL_REQUIREMENTS[i]) {
				cumulative += LEVEL_REQUIREMENTS[i];
				level++;
			} else {
				break;
			}
		}
		return Math.min(level, 20);
	};

	const getLevelProgress = () => {
		let cumulative = 0;
		const level = getCurrentLevel();
		if (level >= 20) return 100;

		for (let i = 0; i < level - 1; i++) {
			cumulative += LEVEL_REQUIREMENTS[i];
		}

		const resultsInCurrentLevel = resultsCount - cumulative;
		const requiredForCurrentLevel = LEVEL_REQUIREMENTS[level - 1];
		return Math.min(
			(resultsInCurrentLevel / requiredForCurrentLevel) * 100,
			100,
		);
	};

	const currentLevel = getCurrentLevel();
	const progress = getLevelProgress();

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

	const handleClearHistory = () => {
		setHistory([]);
	};

	const getOpSymbol = (op: Operation) => {
		switch (op) {
			case "add":
				return "+";
			case "sub":
				return "-";
			case "mul":
				return "×";
			case "div":
				return "÷";
			case "mod":
				return "%";
			case "cos":
				return "cos";
			case "sin":
				return "sin";
			case "mul100":
				return "×100";
			case "div20":
				return "÷20";
			case "mass_kg_lb":
				return "kg→lb";
			case "mass_lb_kg":
				return "lb→kg";
			case "dist_mm_cm":
				return "mm→cm";
			case "dist_cm_mm":
				return "cm→mm";
		}
	};

	const incrementResults = () => {
		setResultsCount((prev) => prev + 1);
	};

	const handleQuickOperation = async (op: Operation) => {
		const currentNum = parseFloat(display);
		const result = await calculate(op, currentNum, 0);
		if (result !== null) {
			const calculation = `${currentNum} ${getOpSymbol(op)} = ${result}`;
			setHistory((prev) =>
				[
					{ id: Math.random().toString(36).substr(2, 9), text: calculation },
					...prev,
				].slice(0, 10),
			);
			setDisplay(result.toString());
			setIsNewEntry(true);
			incrementResults();
		}
	};

	const handleCalculate = async () => {
		if (num1 !== null && operation !== null) {
			const currentNum = parseFloat(display);
			const result = await calculate(operation, num1, currentNum);
			if (result !== null) {
				const calculation = `${num1} ${getOpSymbol(operation)} ${currentNum} = ${result}`;
				setHistory((prev) =>
					[
						{ id: Math.random().toString(36).substr(2, 9), text: calculation },
						...prev,
					].slice(0, 10),
				);
				setDisplay(result.toString());
				setNum1(null);
				setOperation(null);
				setIsNewEntry(true);
				incrementResults();
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
			case "mod":
				return <Percent size={18} />;
			case "cos":
				return <span className="text-xs font-bold">COS</span>;
			case "sin":
				return <span className="text-xs font-bold">SIN</span>;
			case "mul100":
				return <span className="text-xs font-bold">×100</span>;
			case "div20":
				return <span className="text-xs font-bold">÷20</span>;
			case "mass_kg_lb":
				return <span className="text-xs font-bold">kg→lb</span>;
			case "mass_lb_kg":
				return <span className="text-xs font-bold">lb→kg</span>;
			case "dist_mm_cm":
				return <span className="text-xs font-bold">mm→cm</span>;
			case "dist_cm_mm":
				return <span className="text-xs font-bold">cm→mm</span>;
		}
	};

	return (
		<div className="container">
			<div className="main-layout">
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

						<div className="level-counter-container">
							<svg
								className="level-circle"
								viewBox="0 0 36 36"
								role="img"
								aria-labelledby="level-title"
							>
								<title id="level-title">Current Calculation Level</title>
								<path
									className="circle-bg"
									d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
								/>
								<motion.path
									className="circle"
									strokeDasharray={`${progress}, 100`}
									d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
									initial={{ strokeDasharray: "0, 100" }}
									animate={{ strokeDasharray: `${progress}, 100` }}
								/>
								<text x="18" y="20.35" className="level-text">
									{currentLevel}
								</text>
							</svg>
							<span className="level-label label-caps">LVL</span>
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

					<div className="mode-selector">
						<button
							className={`mode-btn ${calcMode === "math" ? "active" : ""}`}
							onClick={() => setCalcMode("math")}
						>
							<CalcIcon
								size={12}
								style={{ display: "inline", marginRight: "4px" }}
							/>{" "}
							Math
						</button>
						<button
							className={`mode-btn ${calcMode === "mass" ? "active" : ""}`}
							onClick={() => setCalcMode("mass")}
						>
							<Weight
								size={12}
								style={{ display: "inline", marginRight: "4px" }}
							/>{" "}
							Mass
						</button>
						<button
							className={`mode-btn ${calcMode === "distance" ? "active" : ""}`}
							onClick={() => setCalcMode("distance")}
						>
							<Ruler
								size={12}
								style={{ display: "inline", marginRight: "4px" }}
							/>{" "}
							Distance
						</button>
					</div>

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
										type="button"
										key={n}
										onClick={() => handleNumber(n)}
										className="btn btn-number glow-hover"
									>
										{n}
									</button>
								),
							)}
							<button
								type="button"
								onClick={handleClear}
								className="btn btn-clear glow-hover"
							>
								<RotateCcw size={18} />
							</button>
						</div>

						<div className="grid-ops">
							{calcMode === "math" && (
								<>
									{(
										[
											"add",
											"sub",
											"mul",
											"div",
											"mod",
											"cos",
											"sin",
										] as Operation[]
									).map((op) => (
										<button
											type="button"
											key={op}
											onClick={() => handleOperation(op)}
											className={`btn btn-op glow-hover ${operation === op ? "btn-op-active" : ""}`}
										>
											{getOpIcon(op)}
										</button>
									))}
									<button
										type="button"
										onClick={() => handleQuickOperation("mul100")}
										className="btn btn-op btn-quick glow-hover"
										disabled={loading}
									>
										{getOpIcon("mul100")}
									</button>
									<button
										type="button"
										onClick={() => handleQuickOperation("div20")}
										className="btn btn-op btn-quick glow-hover"
										disabled={loading}
									>
										{getOpIcon("div20")}
									</button>
									<button
										type="button"
										onClick={handleCalculate}
										className="btn btn-equal glow-hover"
										disabled={loading}
									>
										=
									</button>
								</>
							)}

							{calcMode === "mass" && (
								<>
									<button
										type="button"
										onClick={() => handleQuickOperation("mass_kg_lb")}
										className="btn btn-op btn-quick glow-hover"
										disabled={loading}
									>
										{getOpIcon("mass_kg_lb")}
									</button>
									<button
										type="button"
										onClick={() => handleQuickOperation("mass_lb_kg")}
										className="btn btn-op btn-quick glow-hover"
										disabled={loading}
									>
										{getOpIcon("mass_lb_kg")}
									</button>
								</>
							)}

							{calcMode === "distance" && (
								<>
									<button
										type="button"
										onClick={() => handleQuickOperation("dist_mm_cm")}
										className="btn btn-op btn-quick glow-hover"
										disabled={loading}
									>
										{getOpIcon("dist_mm_cm")}
									</button>
									<button
										type="button"
										onClick={() => handleQuickOperation("dist_cm_mm")}
										className="btn btn-op btn-quick glow-hover"
										disabled={loading}
									>
										{getOpIcon("dist_cm_mm")}
									</button>
								</>
							)}
						</div>
					</div>
				</motion.div>

				<button
					className={`history-toggle-btn ${isHistoryOpen ? "open" : ""}`}
					onClick={() => setIsHistoryOpen(!isHistoryOpen)}
					title="Toggle History"
				>
					{isHistoryOpen ? (
						<ChevronRight size={20} />
					) : (
						<ChevronLeft size={20} />
					)}
				</button>

				<div
					className={`history-panel glass-panel ${isHistoryOpen ? "open" : ""}`}
				>
					<header className="history-header">
						<div className="title-group">
							<HistoryIcon className="icon-primary" size={18} />
							<h2 className="label-caps">Operation History</h2>
						</div>
						<button
							type="button"
							onClick={handleClearHistory}
							className="btn-icon-muted"
							title="Clear History"
						>
							<Trash2 size={14} />
						</button>
					</header>
					<div className="history-list">
						<AnimatePresence initial={false}>
							{history.length > 0 ? (
								history.map((entry) => (
									<motion.div
										key={entry.id}
										initial={{ opacity: 0, x: 20 }}
										animate={{ opacity: 1, x: 0 }}
										className="history-item font-mono"
									>
										{entry.text}
									</motion.div>
								))
							) : (
								<div className="history-empty label-caps">
									No operations recorded
								</div>
							)}
						</AnimatePresence>
					</div>
				</div>
			</div>

			<footer className="footer label-caps">
				Morphic Logic Engine • Tactical Calculator • Sidecar Standard
			</footer>
		</div>
	);
};

export default App;

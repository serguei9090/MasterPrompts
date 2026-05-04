import { useState } from "react";

export type Operation =
	| "add"
	| "sub"
	| "mul"
	| "div"
	| "mod"
	| "cos"
	| "sin"
	| "mul100"
	| "div20"
	| "mass_kg_lb"
	| "mass_lb_kg"
	| "dist_mm_cm"
	| "dist_cm_mm";

interface CalculatorRequest {
	operation: Operation;
	num1: number;
	num2: number;
}

interface CalculatorResponse {
	result: number;
	error: string | null;
}

export const useSidecarBridge = () => {
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState<string | null>(null);

	const calculate = async (
		operation: Operation,
		num1: number,
		num2: number,
	): Promise<number | null> => {
		setLoading(true);
		setError(null);
		try {
			const response = await fetch("http://127.0.0.1:8000/calculate", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({ operation, num1, num2 } as CalculatorRequest),
			});

			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}

			const data: CalculatorResponse = await response.json();

			if (data.error) {
				setError(data.error);
				return null;
			}

			return data.result;
		} catch (err) {
			const message = err instanceof Error ? err.message : "Unknown error";
			setError(message);
			return null;
		} finally {
			setLoading(false);
		}
	};

	return { calculate, loading, error };
};

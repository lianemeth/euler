package main

const gridSize = 20

type point [2]int

func newPoint(a int, b int) point {
	return point{a, b}
}

func (p point) toRight() point {
	return newPoint(p[0], p[1]+1)
}

func (p point) toLower() point {
	return newPoint(p[0]+1, p[1])
}

func search(p point, solutions *map[point]int) int {
	if p[0] == gridSize {
		return 1
	}
	if p[1] == gridSize {
		return 1
	} else {
		v, f := (*solutions)[p]
		if f {
			return v
		} else {
			ri := p.toRight()
			ar := search(ri, solutions)
			(*solutions)[ri] = ar
			lo := p.toLower()
			al := search(lo, solutions)
			(*solutions)[lo] = al
			return ar + al
		}
	}
}
func problem15() int {
	solutions := map[point]int{}
	return search(newPoint(0, 0), &solutions)
}

#!/usr/bin/make

# Fortran
# FC     = gfortran
# FFLAGS = -O3 -fopenmp -lm

# C
CC     = gcc
LFLAGS = -O3 -fopenmp -lm -lcblas

# From all .c files in direcrtory, generate the executable names without .c extension
EXE = $(patsubst %.c,%,$(wildcard *.c))

# Main rule
all: $(EXE)
	@echo -e ""

# Compile each .c file
$(EXE):%:%.c
	@echo -e "\n$(BOLD_RED)Compiling$(RESET): $(BOLD_BLACK)$<$(RESET)"
	$(CC) $< -o $@ $(LFLAGS)

# Clean rule
.PHONY: clean
clean:
	rm -f $(EXE)

# Variables to control ANSI escape code
BOLD_BLACK = \033[1m
BOLD_RED   = \033[1;31m
RESET      = \033[0m
